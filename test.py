import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(3)
xbmc.sleep(200)
while xbmc.sleep(200):

      xbmc.executebuiltin( "Container.Refresh" )
print "container refrescado"
