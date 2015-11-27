import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
xbmc.sleep(100)
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
REMOTENOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "remotenoback.xml")
APPCNOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "appcnoback.xml")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/noback.xml", NOBACKDESTFILE )
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/remotenoback.xml", REMOTENOBACKDESTFILE)
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/appcnoback.xml", APPCNOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(1)
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(3)
try:
   os.remove(NOBACKDESTFILE)
   os.remove(REMOTENOBACKDESTFILE)
   os.remove(APPCNOBACKDESTFILE)
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

