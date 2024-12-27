day = int(input("введите дату: ")) # Вводим данные с клавиатуры(дату и месяц) 
month = int(input("введите месяц: "))
# Используем операторы ветвления if elif else для определение сезона и выводим значения 
if 1 <= day <= 31 and month == 3 or 1 <= day <= 30 and month == 4 or 1 <= day <= 31 and month == 5: #проверяем введенные данные для весны
    print("весна")
elif 1 <= day <= 30 and month == 6 or 1 <= day <= 31 and month == 7 or 1 <= day <= 31 and month == 7: #проверяем введенные данные для лето
    print ("лето")
elif 1 <= day <= 30 and month == 9 or 1 <= day <= 31 and month == 10 or 1 <= day <= 30 and month == 11: #проверяем введенные данные для осени
    print ("осень")
elif 1 <= day <= 31 and month == 12 or 31 >= day >= 1 and month == 1 or 1 <= day <= 28 and month == 2: #проверяем введенные данные для зимы
    print ("зима") 
    # Если ввели не существующий месяц или дату выводим error
else: print("error")
