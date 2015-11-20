import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
timeout_start = time.time()
timeout = 3
while time.time() < timeout_start + timeout:
      
      xbmc.executebuiltin( "Container.Refresh" )
      
      break  



  

     
      
      
      

