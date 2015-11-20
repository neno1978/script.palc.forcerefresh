import xbmc, time
from subprocess import Popen
xbmc.executebuiltin( "XBMC.Action(back)" )
process = Popen( xbmc.executebuiltin( "Container.Refresh" ))
process.wait()
  

     
      
      
      

