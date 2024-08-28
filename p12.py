#Number of vowels/ consonant/uppercase/lowercase characters in the text file

def countstr():
  f=open("info p12.txt","r")
  v=c=u=l=0
  data=f.read()
  for i in data:
    if i.isalpha():
      if i.isupper():
        u+=1
      elif i.islower():
        l+=1
      if i.lower() in 'aeiou':
        v+=1
      else:
        c+=1
  print("No. of vowels are:",v)
  print("No. of uppercases are:",u)
  print("No. of lowercases are:",l)
  print("No. of consonants are:",c)
countstr()
