import Garden
from FilesUtiles import write_to_file, read_from_file

# inp=input("1:new garden\n2:open garden\n")
#
# while inp != "1" and inp != "2":
#     print("wrong input")
#     inp = input("1:new garden\n2:open garden\n")
# if inp == "1":
#     garden = Garden.Garden()
#     garden.play()
# elif inp == "2":
#     garden = Garden.Garden(read_from_file())
garden=Garden.Garden()
garden.test()
print(garden.plants)
print(garden.to_dict())
write_to_file(garden.to_dict())
