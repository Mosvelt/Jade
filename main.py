with open("example.jde", "r") as file:
      var_dict={}
      func_dict={}
      end_of_file = False
      lines_read = 0
      buffer = file.read().split(" ")
      file_length = len(buffer)

      for index, character in enumerate(buffer):
        if character == "print":
          print(buffer[index+1])
          

  
'''while lines_read < file_length:
        print(buffer[lines_read])
        if(buffer[lines_read].split == "print"):
          
          for x in range(1, len(buffer.split(" "))):
            
            print(buffer.split(" ")[x], end = "")
          
          print("")
        
        lines_read+=1'''
      #while(end_of_file == False):
"""buffer = file.readline().split(" ")
        if(buffer[0] == "End"):
          end_of_file = True
          continue
        elif(buffer[0] == "print"):
          for x in range(1, len(buffer)):
            print(buffer[x], end="")
          print("")
          continue
        
        #var_dict[buffer[0]] = buffer[1]"""
