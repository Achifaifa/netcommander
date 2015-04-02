"""
Networking module with network functions
"""

import os, subprocess

def ping(host):
  """
  Pings a host 2 times. Returns 1 if the ping is successful, 0 otherwise
  
  The host needs to be a string containing an IP address 
  """

  return not os.system('ping -c 2 '+host+'>/dev/null')

if __name__=="__main__":
  pass
