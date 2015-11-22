import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
xbmc.executebuiltin( "XBMC.Action(back)" )
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
CUSTOMKEYDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customkey.xml")

urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/noback.xml", NOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
xbmc.executebuiltin( "Container.Refresh" )
try:
   os.remove(NOBACKDESTFILE)
except:
   pass    


xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

