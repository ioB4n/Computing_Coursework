def read(number_list):
    try:
        num_list = number_list[:]
        with open("grades.txt") as file:
            content = file.read()
            content = content.lower()
            for ch in "qwertyuiopasdfghjklzxcv\nbnm! #$%&\"()*+-./:;<=>?@[\\]^_`{|}~'":
                content = content.replace(ch, '')
            if ',' in content:
                numbers = content.split(',')
                for num in numbers:
                    if num.isdigit():
                        num = int(num)
                        if num >= 0 and num <= 100:
                            num_list.append(num)
            else:
                if content.isdigit():
                    content = int(content)
                    if content >= 0 and content <= 100:
                        num_list.append(content)
        return num_list
    except FileNotFoundError: 
        return num_list
    except Exception as e:
        print("AN ERROR OCCURED:", e)
    
def main():
    number_list = []
    number_list = sorted(read(number_list))
    print(number_list)
    with open("grades.txt", 'w+') as file:
        file.write("Grades: ")
    with open("grades.txt", 'a') as file:
        for index, num in enumerate(number_list):
            if index == len(number_list) - 1:
                file.write(str(num) + ';')
            else:
                file.write(str(num) + ',')

main()
