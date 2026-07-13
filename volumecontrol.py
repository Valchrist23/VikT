volume=50
op=0

while op != 3:

    print ("Config")
    print("current volume", volume)

    print ("1 volume up")
    print ("2 volume down")
    print ("3 menu out")

    op = int(input("what option do you want? "))

    match op:
        case 1:
            print("volume up")

            if volume<100:
                volume+=5

        case 2:

            print("volume down")

            if volume>0:
                volume-=5

        case 3:

            print("menu out")

        case _:
            print("Invalid Action")
