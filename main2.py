def has_symbols(password):
    return True in [not simbol.isdigit() and not simbol.isalpha() for simbol in password ]

def has_digit(password):
    return True in [simbol.isdigit() for simbol in password ]

def has_letters(password):
    return True in [simbol.isalpha() for simbol in password ]

def has_upper_letters(password):
    return True in [simbol.isupper() for simbol in password ]

def has_lower_letters(password):
    return True in [simbol.islower() for simbol in password ]

def is_very_long(password):
    if (len(password)) > 11:
        return True
    else:
        return False

if __name__ == '__main__':
    password = input("Введите пароль: ")

    password_check = [  
    has_digit , is_very_long , has_letters , has_lower_letters , has_upper_letters, has_symbols]

    score = 0
    for check in password_check :
        if check(password):
            score += 2

    print (f"Рейтинг пароля: {score}")