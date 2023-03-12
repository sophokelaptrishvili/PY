#define the function
def mainMes():
    #type the question for the input and give 2 options 
    message = input("How's your day? Good- :), Bad- :(  ")

    #print specific text according to different criterias
    if ":(" in message:
        print("So sorry to hear that you're having a bad day", message.replace(":(", "🙁"), "Everything is going to be allright!💛")


    if ":)" in message:
        print("Glad to hear that you're having a good day", message.replace(":)", "🙂 " ), "Keep going like this🚀")

mainMes()






