#1 задание
print("Введите номер квартиры")
room = int(input())

stage =  int(room//8+1)
floor = int(room-(stage-1)*8)


if (room % 8) == 0:
 print(stage-1, floor+8)
else:
 print(stage, floor)