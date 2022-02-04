import webbrowser
import time

#our typical pairing session lasted four hours 
#so lets have two breaks during that time

BREAKS = 1
# we use the range function which includes zero, thats why it is set to one and not two
# we have a total of two breaks every 1.5hours or 5400 seconds
for i in range(BREAKS):
  time.sleep(90*60) # computer asleep for 1.5 hours until we need to open browser
  webbrowser.open("https://www.youtube.com/watch?v=ZJ2tcji7O64", new = 2, autoraise = True)
  #opens this url in a new window every 1.5 hours for a total of two times