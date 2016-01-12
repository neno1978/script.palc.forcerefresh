import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
xbmc.executebuiltin( "XBMC.Action(back)" )
APPCOMMANDDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customapp.xml")
try:
   os.remove(APPCOMMANDDESTFILE)
except:
   pass
TESTPYDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "test.py")
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
REMOTENOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "remotenoback.xml")
APPNOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "appnoback.xml")
SEARCHDESTIFILE= os.path.join(xbmc.translatePath('special://userdata/keymaps'), "search.txt")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/noback.xml", NOBACKDESTFILE )
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/remotenoback.xml", REMOTENOBACKDESTFILE)
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/appnoback.xml", APPNOBACKDESTFILE )
APPCOMMANDDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customapp.xml")
xbmc.executebuiltin('Action(reloadkeymaps)')
time.sleep(1)
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(3)
try:
   os.remove(NOBACKDESTFILE)
   os.remove(REMOTENOBACKDESTFILE)
   os.remove(APPNOBACKDESTFILE)
   if os.path.exists ( TESTPYDESTFILE ):
       urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.palc.forcerefresh/master/Bricocine/customapp.xml", APPCOMMANDDESTFILE )
       xbmc.executebuiltin('Action(reloadkeymaps)')
   xbmc.executebuiltin('Action(reloadkeymaps)')    
   else:
      xbmc.executebuiltin('Action(reloadkeymaps)') 
      print "no testpy"
except:
   pass    
xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

