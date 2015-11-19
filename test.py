import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(3)
timeout = time.time() + 3
while time.time() < timeout:
      test = 0
      if test == 5 or time.time() > timeout:
          xbmc.executebuiltin( "Container.Refresh" )
          break
     
      
      
      

