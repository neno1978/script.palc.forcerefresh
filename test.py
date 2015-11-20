import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
process = xbmc.executebuiltin( "Container.Refresh" )
process.wait()
  

     
      
      
      

