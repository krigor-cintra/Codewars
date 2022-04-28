"""You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
 Write a method that takes the array as an argument and returns this "outlier" N."""

def find_outlier(integers):
  p = 0
  i = 0
  outlier = 0
  axu=0
  axui=0
  for n in range(len(integers)):
    if ((integers[n])%2==0):
        p=p+1
        axu=integers[n]
    elif ((integers[n])%2!=0):
        i=i+1
        axui=integers[n]
  print(i,p)
  if(i==1):
    outlier=axui
  elif(p==1):
    outlier=axu
  return outlier
