import sys
import os
import json
import base64
import re
import urllib
import urllib2
import cookielib
import bencode
import hashlib 
import logging
import xbmc

USERNAME = ""
PASSWORD = ""

PAYLOAD = json.loads(base64.b64decode(sys.argv[1]))
COOKIE = xbmc.translatePath("special://masterprofile/addon_data/plugin.video.pulsar/tl.provider.cookie")

URL_TL = "http://www.xbytes.li/index.php"
URL_SEARCH = "http://www.xbytes.li/browse.php?search=%s"

CATEGORY_MOVIES = "1,11,13,14"
CATEGORY_EPISODES = "26"

login_data = urllib.urlencode({
  'username' : ,
  'password' : 
})

cj = cookielib.MozillaCookieJar(COOKIE)

def get_opener():
  if os.access(COOKIE, os.F_OK):
    cj.load(ignore_discard=True)
    
  opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cj)
  )
  opener.addheaders = [
    ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                   'Windows NT 5.2; .NET CLR 1.1.4322)'))
  ]
  
  return opener

def get_data(url):
  opener = get_opener()
  
  response = opener.open(url)
  content = ''.join(response.readlines())
  
  if not logged_in(content):
    print "Not logged in"
    
    # login
    response = opener.open(URL_TL, login_data)
    content = ''.join(response.readlines())
  
    # check login again
    if not logged_in(content):
      return ""
      
    # login success, save session and reload
    cj.save(ignore_discard=True)
    content = get_data(url)
    
  return content

def logged_in(content):
  if content.find("loginform") > 0:
    return False
  else:
    return True
    
def get_torrent_data(torrent_url):
  content = get_data(torrent_url)
  logging.debug(content)
  metadata = bencode.bdecode(content)
  return metadata
  
def get_data_hash(metadata):
  meta_info = bencode.bencode(metadata["info"])
  meta_info_digest = hashlib.sha1(meta_info).digest()
  return base64.b32encode(meta_info_digest)
  
def get_data_trackers(metadata):
  data = []
  if "announce-list" in metadata:
    for item in metadata["announce-list"]:
      data.extend(item)
  elif "announce" in metadata:
    data.append(metadata["announce"])
    
  return data

def torrent2magnet(torrent_url):
  print "TL: Downloading " + torrent_url
  torrent = get_data(torrent_url)
  metadata = bencode.bdecode(torrent)
  hashcontents = bencode.bencode(metadata['info'])
  digest = hashlib.sha1(hashcontents).digest()
  b32hash = base64.b32encode(digest)
  magneturl = 'magnet:?xt=urn:btih:' + b32hash  + '&dn=' + metadata['info']['name']
  return magneturl
  
def search(query, category=""):
  data = get_data(URL_SEARCH % (urllib.quote_plus(query), category))
  """
  rPayload = []
  for torrent in re.findall(r'/download/.*\.torrent', data):
    print os.path.join(URL_TL, torrent)
    torrent_data = {}
    metadata = get_torrent_data(os.path.join(URL_TL, torrent))
    torrent_data["name"] = metadata["info"]["name"]
    torrent_data["info_hash"] = get_data_hash(metadata)
    torrent_data["trackers"] = get_data_trackers(metadata)
    rPayload.append(torrent_data)
    
  print rPayload
  return rPayload
  """
  
  """ TEMPORARILY RETURN MAGNETS (MAX 5) """
  count = 0
  MAX_TORRENTS = 2
  rPayload = []
  for torrent in re.findall(r'/download/.*\.torrent', data):
    count += 1
    rPayload.append({"uri": torrent2magnet(URL_TL + torrent)})
    if count >= MAX_TORRENTS:
      break
      
  return rPayload

def search_episode(imdb_id, tvdb_id, name, season, episode):
  # search only for episodes
  return search("%s S%02dE%02d" % (name, season, episode), CATEGORY_EPISODES)

def search_movie(imdb_id, name, year):
  # SD and HD movies are categorized, and we can't search multiple categories
  return search(name + " " + year, CATEGORY_MOVIES)

#print json.dumps(globals()[PAYLOAD["method"]](*PAYLOAD["args"]))
urllib2.urlopen(
    PAYLOAD["callback_url"],
    data=json.dumps(globals()[PAYLOAD["method"]](*PAYLOAD["args"]))
)
