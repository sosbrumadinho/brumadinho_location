import os
from  service.settings.common import *

ALLOWED_HOSTS = ["*"]

DEBUG = True

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}


flag = """
                 +-+-+-+-+-+              
                 |U|s|i|n|g|              
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |D|e|v|e|l|o|p|m|e|n|t| |S|e|t|t|i|n|g|s|
 +-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+
 """

print(flag)