#!/usr/bin/env python

import networking, process, wins

# Load hosts
hosts=process.loadhosts()

# Main menu
def menu():
  """
  Main menu
  """

  while 1:
    wins.printcycle(hosts)
    raw_input()


if __name__=="__main__":
 
  try: 
    menu()
    print "test"
  # except Exception,e:
  #   print e
  finally:
    wins.exitp()
