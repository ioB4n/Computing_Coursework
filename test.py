def read(number_list):
    with open("grades.txt") as file:
        number = file.read()
        number = number.lower()
        for ch in "qwertyuiopasdfghjklzxc v\nbnm!#$%&\"()*+-./:;<=>?@[\\]^_`{|}~'":
            number = number.replace(ch, '')
        if ',' in number:
            numbers = number.split(',')
            for num in numbers:
                if num.isdigit():
                    num = int(num)
                    if num >= 0 and num <= 100:
                        number_list.append(num)
def main():
    number_list = []
    read(number_list)
    number_list.sort()
    print(number_list)
    with open("grades.txt", 'w+') as file:
        file.write("Grades: ")
    with open("grades.txt", 'a') as file:
        for num in number_list:
            file.write(str(num) + ',')

main()
