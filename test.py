import xbmc, time
time_start= time.time()
timeout = time.time() + 3

while time.time() < time_start + timeout:
      xbmc.executebuiltin( "XBMC.Action(back)" )
      time.sleep(1)
      xbmc.executebuiltin( "Container.Refresh" )
      time.sleep(2)
      break            



  

     
      
      
      

