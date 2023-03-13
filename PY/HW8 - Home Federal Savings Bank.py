def greeting():
    greet = input("Greet the user:").lower()

# check if the greeting starts with Hello or H 
# and define the output accordingly
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h"):
        print("$20")
    else:
        print("$100")

greeting()
