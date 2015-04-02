#!/usr/bin/env python

import networking, process, wins

# Load hosts
hosts=process.loadhosts()

# Initialize curses screen

# Main menu
def menu():
  """
  Main menu
  """

  pass

def initall():
  """
  Sets the initial conditions for the program to run
  """

  context=wins.init()

if __name__=="__main__":
  initall()
  menu()
