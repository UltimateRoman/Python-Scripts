import time

t1 = time.time()
print("Timer started at ",time.localtime().tm_hour, " hours ",time.localtime().tm_min," mins")
print("\n1.Stop")
print("2.Lap start")
while True:
 c = int(input())
 if c==1:
  t2 = time.time()
  print("\nTotal time period: ",(t2-t1)/60, " mins")
  break
 elif c==2:
  tl = time.time()
  w = input()
  if w == 's':
      print("\nLap time: ", (time.time()-tl)/60, " mins")

time.sleep(5)
