def nitro(boost_amount):
    user_input = input("Do you really want to boost? Y/N...")
    if user_input.lower() == "y":
        print("boost")
    else:
        print("Never mind")


nitro(100)