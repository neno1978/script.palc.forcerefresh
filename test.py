import xbmc, time
xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(3)
xbmc.executebuiltin( "Container.Refresh" )
print "Container refrescado"      

