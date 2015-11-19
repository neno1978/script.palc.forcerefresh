import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(3)
timeout = time.time() + 3
while time.time() < timeout:
      xbmc.executebuiltin( "Container.Refresh" )
print "container refrescado"      
      
      
      

