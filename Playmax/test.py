import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/noback.xml", NOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(1)
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(1)
try:
   os.remove(NOBACKDESTFILE)
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)')
