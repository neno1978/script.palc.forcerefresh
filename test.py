import xbmc, time
from subprocess import popen
xbmc.executebuiltin( "XBMC.Action(back)" )
process = popen( xbmc.executebuiltin( "Container.Refresh" ))
process.wait()
  

     
      
      
      

