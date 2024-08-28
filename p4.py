#Program to display frequency of every element
def freqcount(l):
  freq={}
  for item in z:
    if (item in freq):
      freq[item]+=1
    else:
      freq[item]=1
  print(freq)
z=[1,2,3,3,3,5,6,7,7]
freqcount(z)
