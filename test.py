import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
timeout_start = time.time()
timeout = 3
while time.time() < timeout_start + timeout:
      test = 0
      xbmc.executebuiltin( "Container.Refresh" )
      if test == timeout:
         break  



  

     
      
      
      

