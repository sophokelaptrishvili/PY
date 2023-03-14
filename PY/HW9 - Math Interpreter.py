def mathInt():
 #ask the user for the calculation and convert the inputted data into list
    userQues = input("Put your math problem in here:")
    x, y, z = userQues.split()
   
 #convert numbers into float
    floatX = float(x)
    floatZ = float(z)

 #define the conditions and output accordingly
    if y == "+":
        result = floatX + floatZ

    if y == "-":
        result = floatX - floatZ

    if y == "/":
        result = floatX / floatZ
    
    if y == "*":
        result = floatX * floatZ
       
      
 #print the final calculation
    print(round(result, 2))
    
    
   

mathInt()
