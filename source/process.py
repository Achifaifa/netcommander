"""
This module processes information files
"""

import os

def loadhosts():
  """
  Loads the /etc/hosts file. If the file is not found, it looks

  for a hosts file in the data directory (See example file)
  """

  path="/etc/hosts" if os.path.isfile("/etc/hosts") else "../data/hosts"
  with open(path,"r") as hosts:
     hostsdict={line.partition(' ')[0].strip():line.partition(' ')[2].strip() for line in hosts if (not line.startswith('#') and not ":" in line and line.strip())}
  return hostsdict

if __name__=="__main__":
  pass
