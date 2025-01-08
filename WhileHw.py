import turtle
t=turtle.Turtle()
tscreen=turtle.Screen()
while True:
    command=tscreen.textinput("Enter directions or exit","Enter a direction : forward, backward ,left,right or type quit to exit the game ").lower()
    if command == "forward":
        t.goto(0,0)
        t.forward(100)
    elif command == "left":
        t.goto(0,0)
        t.left(90)
        t.fd(100)
    elif command == "right":
        t.goto(0,0)
        t.right(90)
        t.fd(100)
    elif command == "backward":
        t.goto(0,0)
        t.backward(100)
    elif command == "quit":
        break
        print("thanks for playing!!!!")
    else:
        print("Invalid command. Please try again.")
