a=input()
b=input()
if a=="rock" and b=="paper":
    print("b is winner")
elif a=="rock" and b=="scissor":
    print("a is winner")
elif a=="paper" and b=="rock":
    print("a is winner")
elif a=="paper" and b=="scissor":
    print("b is winner ")
elif a=="scissor" and b=="rock":
    print("b is winner")
elif a=="scissor" and b=="paper":
    print("a is winner")
else:
    print("tie")
