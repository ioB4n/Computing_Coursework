def check_number(num, num_list):
    if num.isdigit():
        num = int(num)
        if num <= 100:
            num_list.append(num)
            print(">>> Added", num, "to the list.")
        else:
            print(">>> Number must be smaller than 100!")
            print(">>> Didn't add", num, "to the list.")
    else:
        print(">>>", num, "is not a valid number!")
    return num_list

def get_number_list(number_list):
    num_list = number_list
    #The list of numbers at this point can either be empty or contain at least 2 elements.
    while len(num_list) < 2:
        print(">>> For multiple numbers, separate using a comma(,).")
        number = input(">>> Input number(s): ").strip()
        if ',' in number:
            number = number.split(',')
            for num in number:
                num_list = check_number(num, num_list)
            print("******************************************")# Adding a separation line.
        else:
            num_list = check_number(number, num_list)
            print("******************************************")# Adding a separation line.
    while True:# Starting a while loop with a constant condition.
        answer = input(">>> Add number(s) to the list? Y/N: ")# Confirming that the user wants to add a number to the list.
        if answer == 'Y' or answer == 'y':# Checking if the user inputs 'Y' or 'y'.
            print(">>> For multiple numbers, separate using a comma(,).")
            number = input(">>> Input number(s): ").strip()# Getting the number, and getting rid of any white spaces.
            if ',' in number:
                number = number.split(',')
                for num in number:
                    num_list = check_number(num, num_list)
                print("******************************************")# Adding a separation line.
            else:
                num_list = check_number(number, num_list)
                print("******************************************")# Adding a separation line.
        elif answer == 'N' or answer == 'n':# Checking if the user inputs 'N' or 'n'.
            print("******************************************")# Adding a separation line.
            break# Breaking out of the while loop.
        else:# Will execute if the user inputs anything other than 'Y', 'y', 'N' or 'n'.
            print(">>> Enter valid response!")
    return num_list

def get_mean(number_list):
    mean = sum(number_list)/len(number_list)
    return mean

def get_median(number_list):
    num_list = number_list[:]
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    while True:
        if len(num_list) > 2:
            del num_list[0]
            del num_list[len(num_list)-1]
        elif len(num_list) == 2:
            median = sum(num_list) / 2
            break
        else:
            median = num_list[0]
            break
    return median

def get_mode(number_list):
    num_list = number_list[:]
    modes = []
    freqs = []
    num_dic = {}
    for num in num_list:
        if num in num_dic:
            num_dic[num] += 1
        else:
            num_dic[num] = 1
    for key in num_dic:
        value = num_dic[key]
        if value not in freqs:
            freqs.append(value)
    if len(freqs) > 1:
        max_freq = max(freqs)
        for key in num_dic:
            if num_dic[key] == max_freq:
                modes.append(key)
    return modes

def get_skew(number_list, mean, median):
    num_list = number_list[:]
    sum_of_difs = 0
    for num in num_list:
        sum_of_difs += pow(num - mean, 2)
    stan_div = pow(sum_of_difs/len(num_list), 1/2)
    skew = (3*(mean-median))/stan_div
    return skew

def main():
    number_list = []
    print("******************************************")# Adding a separation line.
    number_list = get_number_list(number_list)
    while True:
        print("1. Get the MEAN.")
        print("2. Get the MEDIAN.")
        print("3. Get the MODE.")
        print("4. Get the SKEWNESS.")
        print("5. Display the list.")
        print("6. Add more numbers to list.")
        print("Enter q to quit...")
        choice = input(">>> Choice: ")
        print("******************************************")# Adding a separation line.
        if choice == '1':
            print(">>> The MEAN is: " + str(get_mean(number_list)))
            print("******************************************")# Adding a separation line.
        elif choice == '2':
            print(">>> The MEDIAN is: " + str(get_median(number_list)))
            print("******************************************")# Adding a separation line.
        elif choice == '3':
            modes = get_mode(number_list)
            if len(modes) == 0:
                print(">>> There is no MODE.")
                print("******************************************")# Adding a separation line.
            elif len(modes) == 1:
                print(">>> The MODE is:", modes[0])
                print("******************************************")# Adding a separation line.
            else:
                print(">>> The MODES are:", *modes)
                print("******************************************")# Adding a separation line.
        elif choice == '4':
            print(">>> The SKEWNESS is: " + str(get_skew(number_list, get_mean(number_list), get_median(number_list))))
            print("******************************************")# Adding a separation line.
        elif choice == '5':
            for i in range(len(number_list)):
                for j in range(i + 1, len(number_list)):
                    if number_list[i] > number_list[j]:
                        number_list[i], number_list[j] = number_list[j], number_list[i]
            print(">>> Grades", number_list)
            print("******************************************")# Adding a separation line.
        elif choice == '6':
            number_list = get_number_list(number_list)
        elif choice == 'q':
            break
        else:
            print(">>>", choice, "is not an option!")
            print("******************************************")# Adding a separation line.
    
main()
