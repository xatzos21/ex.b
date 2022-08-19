#  one person
#  decision pyramids that alter the path
#  teasing comments and wordplays in between


print("__________________________", "\n",
      "\n", "New best friend life coaching", "\n",
      "_________________________", "\n")

print("Through the next pair of questions....", "\n")
print("...the future of your new best friend will be decided ...", "\n")
print("...be friendly with your NEW BEST FRIEND :)", "\n")

x = str(input("Enter name of your new friend!"))

print("\n", "Your new best friend name is:", x)
print("\n", x , "is a profesional athlete ")
print("\n", "at the next game ", x, " falls down and...")
print("\n", x," a) breaks a leg ", "b) breaks the spine ", "c) gets a scratch", "\n")

y = str(input("What happens? "))

if y == "c":
    print("\n", "You where to kind with your friend!")
    print("\n", "Start again!")

elif y == "b":
    print("\n","OW, thats pretty bad!")
    print("\n", "But life continues as always..")
    print("\n", x, " a) gets over it", "b) gets really depressive", "\n")
    
    z = str(input("And now what? "))
    if z == "a":
        print("\n", "After a long recovery time ", x, " returns healthy back in action :)")
    elif z == "b":
        print("\n", x, " struggles with life due to the injury..")
        print("\n", " a) and starts drinking", " b) but finds the inner strength to become a coach", "\n")
        a = str(input("Keep going: "))
        if a == "a":
            print("\n", "After a long dark time the end comes for ", x)
            print("\n", x, " didn't went pretty far!")
        elif a == "b":
            print("\n", x, " manages to make a second successful carrier as coach")
    else: 
        print("\n", "Wrong answer, again!")

elif  y == "a":  
        print("\n", " It could had been worst!")
else:
    print("\n", "Wrong answer!", "\n", "Again!")