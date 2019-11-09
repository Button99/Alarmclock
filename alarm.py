import sys
from time import sleep

def Time(h,m,s):
  if h<0:
      print("Invalid number at hours")
      print("Closing program")
      sys.exit(0)
  if m<0:
      print("Invalid number  at minutes")
      print("Closing program")
      sys.exit(0)
  if s<0:
      print("Invalid number at seconds")
      print("Closing program")
      sys.exit(0)
  h=h*3600
  m=m*60
  s=h+m+s
  alarm(s)

def alarm(Seconds):
    print("Wait time",Seconds, "Seconds")
    sleep(Seconds)
    sound()

def sound():
    try:
      for i in range(10):
          print(chr(7))
          sleep(1)
    except KeyboardInterrupt:
      print("Interrupted by user")
      sys.exit(1)

print("Welcome to Alarm-Clock Program")
print("Hours: ")
hours=int(input())
print("Minutes")
minutes=int(input())
print("Seconds")
seconds=int(input())
Time(hours,minutes,seconds)

