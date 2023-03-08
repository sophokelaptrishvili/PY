

def greetingSmb():
    
 # ask for the name Uppercase  
    name = input("What's your name?").title()

 # remove extra whitespaces & concatenate    
    clear = " ".join(name.split())
    concat = "Hello, "+ str(clear) +", nice to meet you!"
    
 # print the output 
    print(concat)
   
greetingSmb()


