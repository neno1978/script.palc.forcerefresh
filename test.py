import xbmc, time
import subprocess
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(3)
subprocess.call (xbmc.executebuiltin( "Container.Refresh" ))     

     
      
      
      

