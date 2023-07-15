# main.py

def validator(s):
  parentheses = {"(": ")", "[": "]", "{": "}"}
  OP = [] 

  for letter in s:
    if letter in parentheses:
      OP.append(letter) 
    if letter in parentheses.values():
      
      if len(OP) == 0:
        return False
      if letter != parentheses[OP.pop()]:
        return False
  if len(OP) > 0:
    return False
  if len(OP) == 0:
    return True
    
    
def validator_recursive(s):
  a = list(s) 
  if len(s) == 0:
    return True
  if len(s) == 1:
    return False
  for i in range(len(s)-1):  
    thingy = s[i] + s[i+1] 
    if thingy == "()" or thingy == "[]" or thingy == "{}": 
      return validator_recursive(s[0:i] + s[i+2:]) 
  return False 
    
  


  

string = input("Enter a set of parentheses: ")   
print(validator(string))
print(validator_recursive(string))

