number_of_day = 0
week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение')
for day in week:
    number_of_day+=1
    if number_of_day == 6 or number_of_day == 7:
        status = "Выходной"
    else:
        status = "Рабочий"
    print(day, number_of_day, status)