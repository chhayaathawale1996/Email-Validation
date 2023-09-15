Email = input("Enter your Email :")
space = 0
upper_char = 0
special_char = 0
if len(Email) >= 6 :          # length of email id should be 6 or greater than 6
   if Email[0].isalpha():
       if ("@" in Email) and (Email.count('@')==1):
           if (Email[-4]==".") ^ (Email[-3]=="."):              # in EXOR operator(^) T+T= F, F+F = F ,T+F = T, F+T=T
               for char in Email:
                   if char == char.isspace():
                       space = 1
                   elif char.isalpha():
                       if char == char.upper():
                           upper_char = 1
                   elif char.isdigit():
                       continue
                   elif char == "_" or char == "." or char == "@":
                       continue
                   else:
                       special_char = 1

               if space == 1 or upper_char == 1 or special_char == 1:
                   print("Invalid Email id, please check spaces, special character and case")
               else:
                   print("valid Email id")
           else:
               print("Invalid Email id, check, please check '.' position")
       else:
           print("Invalid Email id, check the count of @ and presence of @")
   else:
       print("Invalid Email id, First character should be alphabetical")
else:
    print("Invalid Email id, length should be greater and equal to six")