"""
Curses window manager
"""

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

def refresh(screens):
  """
  Receives an array of screens and refreshes them in order

  Screens in the background must be first on the list
  """

  for screen in screens: screen.refresh()

if __name__=="__main__":
  pass
