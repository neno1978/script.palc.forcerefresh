import xbmc, time
import urlparse,urllib2,urllib,re
import os, sys
_actions = [
  ["Navigation", [
    "parentfolder"      , "Show Info",
  ]]
from collections_backport import OrderedDict
from utils import rpc
import xbmc


def action_dict(actions, action_names):
    """Create dict of action->name sorted by name"""
    return OrderedDict(sorted(zip(actions, action_names), key=lambda t: t[1]))


def _get_run_addon_actions():
    addons = []
    addon_types = ['xbmc.python.pluginsource', 'xbmc.python.script']
    for addon_type in addon_types:
        response = rpc('Addons.GetAddons', type=addon_type, properties=['name', 'enabled'])
        res = response['result']
        if 'addons' in res:
            addons.extend([a for a in res['addons'] if a['enabled']])
    actions = ['runaddon(%s)' % a['addonid'] for a in addons]
    names = ['Launch %s' % a['name'] for a in addons]
    return action_dict(actions, names)
  
def _get_activate_window_actions():
    all_windows = _activate_window + _windows[2:] #don't include "global"
    actions = ["activatewindow(%s)" % w_id for w_id in all_windows[0::2]]
    names = ["Open %s" % w for w in all_windows[1::2]]
    return action_dict(actions, names)


def _get_action_dict():
    """ Map actions to 'category name'->'action id'->'action name' dict"""
    d = OrderedDict()
    for elem in _actions:
        category = elem[0]
        actions = elem[1][0::2]
        names = elem[1][1::2]
        d[category] = OrderedDict(zip(actions, names))  
ACTIONS = _get_action_dict()
WINDOWS = OrderedDict(zip(_windows[0::2], _windows[1::2]))

xbmc.executebuiltin( "XBMC.Action(back)" )
time.sleep(2)
NOBACKDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "noback.xml")
CUSTOMKEYDESTFILE = os.path.join(xbmc.translatePath('special://userdata/keymaps'), "customkey.xml")

urllib.urlretrieve ("https://raw.githubusercontent.com/neno1978/script.pulsar.xbyte/master/noback.xml", NOBACKDESTFILE )
xbmc.executebuiltin('Action(reloadkeymaps)')
print "Container Refrescado"
xbmc.executebuiltin( "Container.Refresh" )
time.sleep(5)
try:
   os.remove(NOBACKDESTFILE)
except:
   pass    

xbmc.executebuiltin('Action(reloadkeymaps)') 


    



  

     
      
      
      

