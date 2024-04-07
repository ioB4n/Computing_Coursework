with open("grades.txt") as file:
    number = file.read()
    number = number.lower()
    for ch in "qwertyuiopasdfghjklzxcv\nbnm!#$%&\"()*+-./:;<=>?@[\\]^_`{|}~'":
        number = number.replace(ch, ' ')

    stripped_number = number.strip()
    print(stripped_number)
