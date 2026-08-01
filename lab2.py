# A function is used when I want to perform multiple taks without haveing to write numerous lines of code
# I can just create a simple function and stores all those lines of code into one organized block.

def check_password_strength(password):
   if len(password) < 8:
      return "weak ahh password"
   else:
      return "secure password"
   

test_sumation = check_password_strength("DavidOl123")
print(f"The password provided is a {test_sumation}")

    

