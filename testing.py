# --/ Variables \-- #

token = ""
curstr = ""

tokens = []
func_tokens = {}
used_token = False

func = False
isstr = False

pre_index = 0
skip_index = 0

# --/ Parser \-- #

with open("testing.jde", "r") as rfile:
  var_dict={}
  func_dict={}
  end_of_file = False 
  lines_read = 0
  buffer = rfile.read()
  file_length = len(buffer)

  for char in buffer:
    if char == "'" or char == '"':
      if isstr == False:
        isstr = True

      elif isstr == True:
        isstr = False
        tokens.append(curstr)
        curstr = ""
        continue
        
      continue

    if isstr == True:
      curstr += char
      continue
    
    if char == " "or char == ";"or char == "\n":
      tokens.append(token)
      token = ""
      
      continue

    
    token += char

# --/ lexer - Interpereter \-- #

for index, token in enumerate(tokens):
  if token == " ":
    continue
  
  if used_token == True:
    used_token == False
    continue

  if not index >= skip_index:
    continue
    
  elif token == "print" and func == False:
    print(tokens[index+1])
    used_token = True

  elif token == "func":
    if func == False:
      func = True
      
    else:
      print("Cannot assign a function in a function")
      
    func_name = tokens[index+1]
    func_tokens[func_name] = []
    
    for findex, ftoken in enumerate(tokens):
      if ftoken != "end" and ftoken != "}":
        if ftoken != "func" and ftoken != func_name:
      
          func_tokens[tokens[index+1]].append(ftoken)
          skip_index += 1

        else:
          continue
      
      else:
        break

    skip_index += index + 1
    pre_index = index
    func = False

  elif token == "call":
    func_name = tokens[index+1]
    
    if len(func_tokens[func_name]) > 0:
      
      for cindex, tok in enumerate(func_tokens[func_name]):
        if used_token == True:
    
          used_token = False
          continue
          
        if tok == "print" and func == False:
          print(func_tokens[func_name][cindex+1])
          used_token = True
