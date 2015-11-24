import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
_actions = [
  ["Navigation", [
    "parentfolder"      , "Show Info",
  ]]
ACTIONS = _get_action_dict()
WINDOWS = OrderedDict(zip(_windows[0::2], _windows[1::2]))

xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(2)
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
CUSTOMKEYDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customkey.xml")

urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/noback.xml", NOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
print "Container Refrescado"
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(5)
try:
   os.remove(NOBACKDESTFILE)
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

