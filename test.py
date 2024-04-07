with open("grades.txt") as file:
    number = file.read()
    number = number.lower()
    for ch in "qwertyuiopasdfghjklzxcv\nbnm!#$%&\"()*+-./:;<=>?@[\\]^_`{|}~'":
        number = number.replace(ch, ' ')

    number = number.strip()
    
    print(number)
