import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
APPCOMMANDDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customapp.xml")
try:
   os.remove(APPCOMMANDDESTFILE)
except:
   pass
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
REMOTENOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "remotenoback.xml")
APPNOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "appnoback.xml")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/noback.xml", NOBACKDESTFILE )
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/remotenoback.xml", REMOTENOBACKDESTFILE)
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/appnoback.xml", APPNOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(1)
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(3)
try:
   os.remove(NOBACKDESTFILE)
   os.remove(REMOTENOBACKDESTFILE)
   os.remove(APPNOBACKDESTFILE)
   urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/customapp.xml", APPCOMMANDDESTFILE )
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

