# reversing an integer using modulo operator

def reverseInteger(x):
  rev = 0
  negative = 0 # keep track of if negative number
  if x < 0:
    x = x * -1
    negative += 1
  while x > 0:
    remainder = x % 10 # this will divide the number by 10 and give the remainder 
    rev = rev * 10 + remainder
    x = x // 10 # divide and round the result down to the nearest whole number
  if rev <= 10**100: # can be anything. This is just a comparison
    if negative == 1: # handle negative case
      rev = rev * -1
      return rev
    else:
      return rev
  else:
    return 0 # needs to return a value

print(reverseInteger(17876)) # testing
print(reverseInteger(-17076)) # testing 