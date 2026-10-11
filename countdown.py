import time

def convert_seconds(hour, minute, second):
  return hour * 3600 + minute * 60 + second

def countdown():
  hour, minute, second = map(int, input("Enter countdown time(H:M:S): ").split(":"))
  t = convert_seconds(hour, minute, second)
  while t >= 0:
    hrs, remainder = divmod(t, 3600)
    min, secs = divmod(remainder, 60)
    timer = '{:02d}:{:02d}:{:02d}'.format(hrs, min, secs)
    print(timer, end='\n')
    time.sleep(1)
    t -= 1
  print("Timer ends!!")
  
if __name__ == '__main__':
  countdown()