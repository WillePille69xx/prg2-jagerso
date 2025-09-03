def TLM_check():
    while True:
            name = input("Enter your horse's name: ")
            if len(name) < 2:
                print("Name must be at least 2 characters long.")
            else:
                print(f"Your horse's name is {name.capitalize()}.")
                break
TLM_check()