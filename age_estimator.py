year_of_birth = int(input("Introduceti anul nasterii: "))
current_year = int(2020)
current_month = int(7)
calc_birth = current_year - year_of_birth

if year_of_birth < 1900 or year_of_birth > 2020:
    print("Eroare, se permit valori incepand cu anul 1900 pana la anul curent")
    # print(year_of_birth = int(input("Introduceti anul nasterii corect: ")))

elif year_of_birth == 2020:
        print("Anul de nastere introdus: " + str(year_of_birth) + ". Pentru a calcula varsta dumnevoastra este nevoie de a introduce luna de nastere")
        month_of_birth = int(input("Introduceti luna de nastere: "))
        m_y_of_birth = current_month - month_of_birth

        if month_of_birth == 7:
            print("Imposibil de calculat varsta dumnevoastra, sunteti bebelus foarte mic))")
        elif m_y_of_birth == 1:
            print("Luna si anul de nastere introdus: " + str(month_of_birth) + "." + str(year_of_birth) + ".")
            print("Dumnevoastra aveti :" + str(m_y_of_birth) + " luna - sunteti bebelus")
        elif m_y_of_birth >= 1 or m_y_of_birth <= 6:
            print("Luna si anul de nastere introdus: " + str(month_of_birth) + "." + str(year_of_birth) + ".")
            print("Dumnevoastra aveti :" + str(m_y_of_birth) + " luni - sunteti bebelus")

elif year_of_birth == 2019:
        print("Anul de nastere introdus: " + str(year_of_birth) + ". Dumnevoastra aveti: " + str(calc_birth) + " an. Sunteti bebelus")

elif year_of_birth >= 1900 or year_of_birth > 2018:
        print("Anul de nastere introdus: " + str(year_of_birth) + ". Dumnevoastra aveti: " + str(calc_birth) + " ani.")
        if calc_birth >= 2 and calc_birth <= 3:
            print("\tSunteti copil mic.")
        elif calc_birth >= 4 and calc_birth <= 9:
            print("\tSunteti copil.")
        elif calc_birth >= 16 and calc_birth <= 18:
                print("\tSunteti adolescent.")
        elif calc_birth >= 19 and calc_birth <= 50:
                print("\tSunteti adult.")
        elif calc_birth >= 51:
                print("\tSunteti persoana in etate.")
