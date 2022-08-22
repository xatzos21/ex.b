#  one person
#  decision pyramids that alter the path
#  teasing comments and wordplays in between


print("__________________________", "\n",
      "\n", "New best friend life coaching", "\n",
      "_________________________", "\n")

print("Through the next pair of questions....", "\n")
print("...the future of your new best friend will be decided ...", "\n")
print("...be kind with your NEW BEST FRIEND :)", "\n")

x = str(input("Enter name of your new friend! "))

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
    else: 
        print("\n", "Wrong answer, again!")

elif  y == "a":  
        print("\n", " It could had been worst!")
        print("\n", " But simple is the most difficult some times...")
        print("\n", x, " a) from overconfidence messes his recovery", " b) doctor does a wrong OP", "\n")

        b = str(input("Tricky one... "))

        if b == "a":
            print("\n", " Due to that ", x, " team cancels his contract")
            print("\n", x, " a) get the shit together and devotes to the sport", " b) gets addicted to painkillers!", "\n")
            
            c = str(input("Big decision time... "))

            if c == "a":
                print("\n", " But", x, " soon quits professional sport for a long time passion..." )
                print("\n", "...and builds a social-sport center for the neighborhood youth to be trained!", "\n")
            elif c == "b":
                print("\n", " The downfall is absolute until a friend introduces ", x, " to joints")
                print("\n", x, " curates with joints and decides...")
                print("\n", " a) to make a gang"," b) to start an own herbal company to help other professional athletes get over painkillers", "\n")
            
                d = str(input("Interesting... "))

                if d == "a":
                    print("\n", x, " loses control and ends up to jail and the tabloids!", "\n")
                elif d == "b":
                    print("\n", x, " is a legend after the company helped so many people!", "\n")
                else:
                    print("\n", "Wrong answer, again!", "\n")
        elif b == "b":
            print("\n", " The doctor gets fired ", x, " sues the team and breaks his contract!", "\n")
            print("\n", x, " Becomes a legend after gifting the court money to the community, nevertheless earns enough money from sports!", "\n")
        else:
            print("\n", "Wrong answer, again!")
else:
    print("\n", "Wrong answer!", "\n", "Again!")