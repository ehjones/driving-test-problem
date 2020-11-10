# Driving test problem
def passfail(minorfaults):
  
  if minorfaults < 16:
    return "pass"
    
  else:
    return "fail"
  
    
print(passfail(12))
    
