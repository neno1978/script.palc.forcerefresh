import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
CUSTOMKEYDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customkey.xml")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/noback.xml", NOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
time.sleep(1)
xbmc.executebuiltin( "XBMC.Action(back)" )
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(3)
try:
   os.remove(NOBACKDESTFILE)
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)')
