import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" ) 
xbmc.sleep(1000)
KEYMAPDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/noback.xml", KEYMAPDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
time.sleep(1)
xbmc.executebuiltin( "Container.Refresh" )
xbmc.sleep(1000)
KEYMAPDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customkey.xml")
urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/customkey.xml", KEYMAPDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

