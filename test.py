import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep (1)
timeout = time.time() + 3

while timeout < 3:
      
      xbmc.executebuiltin( "Container.Refresh" )
      
      if timeout = 3 :
         break            



  

     
      
      
      

