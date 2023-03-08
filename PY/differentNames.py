


def greetingSmb():

#ask for the name, make it upper case & trim the extra whitespaces    
    name = input("What's your name?").title()
    clear = " ".join(name.split())
#different group of names starting with a
    letterOpt = ("G", "A", "M")
    letterOpt1 = ("S","L", "O")
    letterOpt2 = ("I", "N", "C")



    if name.startswith(letterOpt):
            print("Hello, " + str(clear) + ", nice to meet you!")
           
    elif name.startswith(letterOpt1):
         print("Hi, " + str(clear) + ", nice to meet you!")

    elif name.startswith(letterOpt2):
            print("Hey, " + str(clear) + ", nice to meet you! How are you?")

    else:
        print("Hey, " + str(clear) + ", nice to meet you! Have a good day!")
 
  
   
greetingSmb()


