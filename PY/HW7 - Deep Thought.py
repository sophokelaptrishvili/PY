def deepThought():
   
#ask for the answer from user & clear the answer from extra whitespaces
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    clear = answer.replace(" ", "")
  
#define the conditions in which scenario what to print
    if clear == "42" or clear == "fortytwo" or clear =="forty-two":
        print("yes")
    else:
        print("no")

deepThought() 
