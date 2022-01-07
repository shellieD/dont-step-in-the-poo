from random import randrange


clear_path = randrange(0,8)
print(clear_path)

poos = []
for i in range(8):
    if i != clear_path:
        poos.append((i, randrange(0, 8)))
print(poos)

row = int(input("choose row"))
column = int(input("choose column"))

coord = (row, column)

if coord in poos:
    print("What a mess!!!")
else:
    print("OOooh that was a close one!") 