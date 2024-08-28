def isempty(stk):
  if stk==[ ]:
    return True
  else:
    return False

def push(stk,ele):
  stk.append(ele)
  print("Element inserted..")
  print(stk)

def POP(stk):
  if isempty(stk):
    print("Stack is empty.....")
  else:
    print("Deleted element:",stk.pop())

def Peek(stk):
  if isempty(stk):
    print("Stack is empty...")
  else:
    print("Element at the top is:",stk[-1])

def Display(stk):
  if isempty(stk):
    print("Stack is empty...")
  else:
    for i in range(len(stk)-1,-1,-1):
         print(stk[i])
    
    
stack=[ ]
while True:
  print("************Stack operations**************")
  print("1. PUSH")
  print("2. POP")
  print("3. PEEK")
  print("4. DISPLAY")
  print("5. EXIT")
  choice=int(input("Enter a choice:"))
  if choice==1:
             elt=int(input("Enter an element you want to insert:"))
             push(stack,elt)
  elif choice==2:
    POP(stack)
  elif choice==3:
    Peek(stack)
  elif choice==4:
    Display(stack)
  else:
    choice==5
    break
