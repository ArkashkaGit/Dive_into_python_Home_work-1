# Нерешонная задача с семинара №8
# Нарисовать ёлочку, спросив у пользователя, 
# сколько рядов должно быть у ёлочки 

count_row = int(input("Введите число рядов в треугольнике: "))
count_star = 1
counter = count_row 

while count_star <= count_row*2:
    spase = " "
    star = "*"
    print(spase*counter, star*count_star,end="")
    print("")
    count_star +=2
    counter -= 1