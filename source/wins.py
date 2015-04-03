"""
Curses window manager
"""

import curses
import networking

def init():
  """
  Initializes the curses environment
  """

  scr=curses.initscr()
  curses.noecho()
  curses.cbreak()
  scr.keypad(1)
  if curses.has_colors(): curses.start_color()
  return scr

def exitp():
  """
  Turns off curses environment
  """

  curses.nocbreak()
  curses.echo()
  scr.keypad(0)
  curses.endwin()

def refresh():
  """
  Receives an array of screens and refreshes them in order

  Screens in the background must be first on the list
  """

  for screen in screens: screen.refresh()

def printstatus():
  """
  Prints a status bar on the bottom
  """

  scr.addstr(curses.LINES-1,1,"STATUS BAR BLABLABLA")

def printheader():
  """
  Prints a menu bar
  """

  scr.addstr(0,1,"THIS IS A HEADER")
  scr.chgat(-1,curses.A_REVERSE)

def clearall():
  """
  Clears all the screens
  """

  for s in screens: s.clear()

def printcycle(hosts):
  """
  Clears screens and prnits menus and stuff
  """

  clearall()
  printheader()
  printhosts(hosts)
  printstatus()
  refresh()

def printhosts(hosts):
  """
  Prints all the host on screen
  """

  try:
    for ip, host in hosts.iteritems():
      scr.addstr("[%s]%s\t%s\n"%(ip,host,"UP" if networking.ping(ip) else "DOWN"))
  except: pass

screens=[]
scr=init()
screens.append(scr)

if __name__=="__main__":
  pass
