import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
xbmc.executebuiltin( "XBMC.Action(back)" ) 
time.sleep(2)
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
CUSTOMKEYDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customkey.xml")
try:
   os.remove(CUSTOMKEYDESTFILE)
   print "ck boraddo"
except:
    pass 
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/noback.xml", NOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
time.sleep(1)
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(2)
try:
   os.remove(NOBACKDESTFILE)
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

