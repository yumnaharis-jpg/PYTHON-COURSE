def shutdown(User_input):
    if User_input.lower() == "yes":
        print("shutting down...")
    elif User_input.lower() == "no":
        print("shutdown aborted")
    else:
        print("invalid bro...")
User_input = input("do you wish to shutdown this device? yes/no: ")

print(shutdown(User_input))


