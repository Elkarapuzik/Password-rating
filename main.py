def has_symbols(password):
    mimi = False
    for simvol in password:
        if not simvol.isdigit() and not simvol.isalpha():
            mimi = True
    return mimi 

def has_digit(password):
    mimi = False
    for simvol in password:
        if simvol.isdigit():
            mimi = True
    return mimi

def has_letters(password):
    mimi = False
    for simvol in password:
        if simvol.isalpha():
            mimi = True
    return mimi

def has_upper_letters(password):
    mimi = False
    for simvol in password:
        if simvol.isupper():
            mimi = True
    return mimi

def has_lower_letters(password):
    mimi = False
    for simvol in password:
        if simvol.islower():
            mimi = True
    return mimi

def is_very_long(password):
    if (len(password)) > 11:
        return True
    else:
        return False

password = input("Введите пароль: ")


password_check = [
has_digit , is_very_long , has_letters , has_lower_letters , has_upper_letters, has_symbols]

score = 0
for check in password_check :
    if check(password):
        score += 2

print (f"Рейтинг пароля: {score}")