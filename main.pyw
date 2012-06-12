import sys

original = sys.path[0]
sys.path[0] = sys.path[0] + '\\' + 'System'

import bridge

bridge.mainAppLogin()

sys.path[0] = original


#bridge.mainAppLogin()
