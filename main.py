import time

def gettimeline():
  print('Getting Twitter TimeLine... Please wait.')
  time.sleep(1)
  import gettimeline
def runwc():
  print('Making WordCloud PNG File... Please wait.')
  time.sleep(1)
  import wc
def runptw():
  print('Posting PNG File... Please wait.')
  time.sleep(1)
  import ptw

print('System Start!')
print('Starting Process...')
time.sleep(1)

gettimeline()
runwc()
runptw()

print('Process Done.')
