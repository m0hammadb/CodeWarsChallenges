from ast import arg
from re import I

memoDict = {}

def lcm(*args):
  if(not args):
      return 1
  for item in args:
      if item == 0:
          return 0
  args = list(set(args))
  length = len(args)
  if(length == 1):
      return args[0]
  for i in range(length - 1):
      args[i+1] = fLcm(args[i],args[i+1])
  return args[-1]

def fLcm(a,b):
    if(a > b):
        a,b = b,a
    ini = b
    while ini % a != 0:
        ini += b
    return ini

print(lcm(2,4,6))
    

  
