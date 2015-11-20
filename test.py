import xbmc, time
time_start= time.time()
timeout = time.time() + 3

while time.time() < time_start + timeout:
      xbmc.executebuiltin( "XBMC.Action(back)" )
      xbmc.executebuiltin( "Container.Refresh" )
      xbmc.sleep(200)
      break     



  

     
      
      
      

