with open("input.txt", "r") as file:
    numbers = file.readlines()              # Метод readlines записывает numbers как список чисел из file.

max_length = 0
current_length = 0

for number in numbers:                      #| Этот цикл проверяет является ли число целым числом 3.
    if int(number) == 3:                    #| Если является, то он записывает его в текущую длину,
        current_length += 1                 #| потом сравнивает текущую длину с максимальной,
        if current_length > max_length:     #| если текущая больше, то её значение передаётся максимальной
            max_length = current_length     #| и так до тех пор, пока данные в файле не кончатся.
    else:                                   #| Таким образом программа узнаёт длину самой большой
        current_length = 0                  #| цепи из чисел "3" и записывает её в max_length.

with open("output.txt", "w") as file:
    file.write(str(max_length))