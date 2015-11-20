import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep (1)
time_start= time.time()
timeout = time.time() + 3

while time.time() < timeout_start + timeout:
      
      xbmc.executebuiltin( "Container.Refresh" )
      
      if time.time() == timeout_start + timeout :
         break            



  

     
      
      
      

