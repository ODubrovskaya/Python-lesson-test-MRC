what=input("Хотите узнать, входите ли вы в зону риска? Введите да или нет.")
        if what=="да":
            what=input("Выдерите свой пол. Введите муж или жен")
            if what=="муж":
                a=10
            elif what=="жен":
                a=0
            what=input("Если у вас вторая положительная группа крови, ведите да")
            if what=="да":
                а=10
            else what=="нет":
            what=input("Вы курите?")
            if what=="да":
                c=10
            else what=="нет":
            what=input("Ваша работа связанна с вредными производственными факторами? Такими как: химическое производство, строительная пыль?"
            if what=="да":
                d=10
            else what=="нет":
            what=input("В населенно пункте где вы живете, есть предприятия которые неблагоприятно влияют на окружающую среду, такие как горнодобывающие, металлургические, химические угольные и горнорудная промышленность?")
            if what=="да":
                l=10
            else what=="нет":
        k=(round(a+b+c+d+l))
        print("Ваш результат (k) баллов")
        print("Вы входител в группу риска. Берегите свое здоровье!")
        print("Вы входите в повышенную группу риска. Постарайтесь исключить вредные факторы, такие как курение в том числе и пассивное, ")
        elif what=="нет":
            print("Продолжайте следить за здоровьем. Хорошего дня!")
        else:
            print("Система вас не понимает, введите коректный ответ.")