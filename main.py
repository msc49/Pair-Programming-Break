import webbrowser
import time

#our typical pairing session lasted four hours 
#so lets have two breaks during that time

BREAKS = 1
# we use the range function which includes zero, thats why it is set to one and not two
# we have a total of two breaks every 1.5hours or 5400 seconds
for i in range(BREAKS):
  time.sleep(90*60) # computer asleep for 1.5 hours until we need to open browser