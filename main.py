import Garden



inp=input("1:new garden\n2:open garden\n")

while inp != "1" and inp != "2":
    print("wrong input")
    inp = input("1:new garden\n2:open garden\n")
if inp == "1":
    garden = Garden.Garden()
    garden.play()
elif inp == "2":
    pass


