def read_file(grades_list): # This function is used to try to collect data from a "grades.txt" file that exists on the same directory as the "main.py" file.
    try: # Because we're trying to read data from a file, it makes this function prone to exceptions. So a 'try except' is used.
        with open("grades.txt") as file: # To read the file, 'with open' is used. This is because after executing the code inside the 'with open', the file is automatically closed.
            content = file.read() # Reading the data from the file and storing it as a string into the variable 'content'.
        content = content.lower() # Setting all the alphabetical characters (if any) to lower case, to make it easier to clean the data.
        for ch in "qwertyuiopasdfghjklzxcv\nbnm! #$%&\"()*+-./:;<=>?@[\\]^_`{|}~'": # Iterating thorugh the string of unwanted characters and storing it into 'ch'.
            content = content.replace(ch, '') # Replacing all the occurences of whatever 'ch' is at the moment with nothing, efficiently removing them from 'content'.
        if ',' in content: # At this point, 'content' can only contain numbers or commas. This 'if' statement checks to see if there are any commas in 'content', indicating that there's more than one number.
            numbers = content.split(',') # Spliting the string into multipe individual strings, separating them wherever a comma is found, and storing them into a list 'numbers'
            for num in numbers: # Iterating through the list 'numbers' to verify if each element is a valid number.
                if num.isdigit(): # Making sure that even after the data cleaning, the elements are strings of positive numbers or 0.
                    num = int(num) # Turning the number into an integer for further checking.
                    if num <= 100: # Checking if the number is smaller than 100. The boundaries for the grades are 0 and 100.
                        grades_list.append(num) # Appending the number to list of grades.
        else: # If no commas are in 'content', it indicates that there should be only one string of numbers.
            if content.isdigit(): # Making sure that even after the data cleaning, the elements are strings of numbers.
                content = int(content) # Turning the number into an integer for further checking.
                if content >= 0 and content <= 100: # Checking if the number is between 0 and 100, which are the boundaries for the grades.
                    grades_list.append(content) # Appending the number to list of grades.
    except FileNotFoundError: # Catching any exeptions of type 'FileNotFoundError', which means that there is no such file with the name 'grades.txt'.
        pass # If there is no such file, nothing needs to be done. We continue with an empty list of grades. The user will be asked to input them later.
    except Exception as e: # Catching any other kinds of exeptions, as a means to prevent any unknown potential errors.
        print("AN ERROR OCCURED:", e) # If any other kind of exeption occures, an error message will be printed letting the user know.

def check_number(num, grades_list): # This function is used to check if a number input by the user is valid. If so, the number is appended to the list of grades.
    if num.isdigit(): # Making sure that the string input by the user consits of only positive numbers and 0.
        num = int(num) # Turning the number into an integer.
        if num <= 100: # Checking if the number is within boundaries.
            grades_list.append(num) # Appending the number to the list of grades.
            print(">>> Added", num, "to the list.") # Printing a confirmation message, showing the new grade that was added to the list.
        else: # If the number isn't within boundaries, the following code is executed.
            print(">>> Number must be between 0 and 100!") # Printing an explenatory massage, so the user knows what was wrong with the number.
            print(">>> Didn't add", num, "to the list.") # Printing the number that wasn't added to the list.
    else: # If the string isn't in digit form, the following code is executed.
        print(">>>", num, "is not a valid number!") # Printing an error message.

def add_number_to_list(grades_list): # This function is used to allow the user to add numbers to the list of grades from the terminal.
    while len(grades_list) < 2: # If the list of grades contains less than 2 elements, the user will not be allowed to continue with the program, until they make the list be at least two elements.
        print(">>> For multiple numbers, separate using a comma(,).") # Printing an informational message so the user knows what are the requirements for adding more than one number.
        number = input(">>> Input number(s): ").strip() # Taking the user's input, storing it into 'number', and striping the string of any whitespaces.
        if ',' in number: # If there are commans present in the string 'number', the program assumes that there's supposed to be more than one number.
            numbers = number.split(',') # Spliting the string into multipe individual strings, separating them wherever a comma is found, and storing them into a list 'numbers'
            for num in numbers: # Iterating through the list 'numbers' to check if each each element is a valid number.
                check_number(num, grades_list) # Calling the check_number function to verify the number.
            print("******************************************")# Adding a separation line.
        else: # If there's no commas in 'number', the following code is executed.
            check_number(number, grades_list) # Calling the check_number function to verify the number.
            print("******************************************") # Adding a separation line.
    while True: # Starting a while loop with a constant condition. The reason behind using a constant condition is because the user can choose when to exit the loop, and a 'break' statement will be used.
        answer = input(">>> Add number(s) to the list? Y/N: ") # Confirming that the user wants to add a number to the list and continue going thorugh the loop.
        if answer == 'Y' or answer == 'y': # Checking if the user inputs 'Y' or 'y'.
            print(">>> For multiple numbers, separate using a comma(,).") # Printing an informational message so the user knows what are the requirements for adding more than one number.
            number = input(">>> Input number(s): ").strip() # Taking the user's input, storing it into 'number', and striping the string of any whitespaces.
            if ',' in number: # If there are commans present in the string 'number', the program assumes that there's supposed to be more than one number.
                numbers = number.split(',') # Spliting the string into multiple individual strings, separating them wherever a comma is found, and storing them into a list 'numbers'.
                for num in numbers: # Iterating through the list 'numbers' to check if each each element is a valid number.
                    check_number(num, grades_list) # Calling the check_number function to verify the number.
                print("******************************************")# Adding a separation line.
            else: # If there's no commas in 'number', the following code is executed.
                check_number(number, grades_list) # Calling the check_number function to verify the number.
                print("******************************************")# Adding a separation line.
        elif answer == 'N' or answer == 'n': # Checking if the user inputs 'N' or 'n'.
            print("******************************************") # Adding a separation line.
            break # Breaking out of the while loop.
        else: # Will execute if the user inputs anything other than 'Y', 'y', 'N' or 'n'.
            print(">>> Enter valid response!") # Printing an error message.

def get_mean(grades_list): # This function is used to get the MEAN of the grades.
    mean = sum(grades_list)/len(grades_list) # The MEAN is equal to the sum of all grades devided by the number of grades.
    return mean # Returning the MEAN.

def get_median(grades_list): # This function is used to get the MEDIAN of the grades.
    # To do so, the list must be sorted into ascending or desceding order and a element should be removed from both ends, until only one or two elements remain.
    # If there is only on element, that element is the MEDIAN. If there are tow elements, the MEDIAN is the sum of both devided by 2.
    grade_list = grades_list[:] # Because we will be removing elements from the list, we need to create a copy of the list. 
    # The [:] operator indicates that we are actually creating a new memory location for the new list, not just a reference point to the same location.
    # This way we won't be removing element from the actual list of grades.
    grade_list.sort() # Sorting the list in ascending order using the sort function.
    while True: # Starting an indefinite while loop, as we will exit when we get a MEDIAN value.
        if len(grade_list) > 2: # Checking if the list has more than 2 elements, in which case an element from both ends will be removed.
            del grade_list[0] # Removing the first element from the list.
            del grade_list[len(grade_list)-1] # Removing the last element from the list.
        elif len(grade_list) == 2: # Checking if there are exactly two elements in the list, in which case, the elements are summed and devided by 2.
            median = sum(grade_list) / 2 # Summing the two elements and deviding it by 2.
            break # Now that we have the MEDIAN, we can break from the loop.
        else: # This code is reached only after the first 'if' condition is met at least once. This code is executed if there is only one element left in the list.
            median = grade_list[0] # Getting the MEDIAN.
            break # Breaking out of the loop.
    return median # Returning the MEDIAN.

def get_mode(grades_list): # This function is used to get the MODE(s) from the list of grades. 
    # As there can be more than one MODE, this function is a bit more complex.
    modes = [] # Initiating an empty list for all possible modes.
    unique_freqs = [] # Initiating an empty list for all the existing unique frequencies in the list.
    grades_dic = {} # Initiating an empty dictionary for storing each unique number along with its frequiency.
    for num in grades_list: # We start iterating through the list of grades.
        if num in grades_dic: # We check if the current element exists as a key inside the dictionary.
            grades_dic[num] += 1 # If it does exist, we increment its value (frequency) by 1.
        else: # Otherwise.
            grades_dic[num] = 1 # If it doesn't exist in the dictionary, we add it to the list and set its value to 1.
    for key in grades_dic: # We start iterating through the dictionary, retrieving the keys, which in this case are also the unique grades.
        value = grades_dic[key] # We get the value of that unique grade and story it into a variable 'value'.
        if value not in unique_freqs: # We check if the value doesn't already exist inside the list of unique frequencies.
            unique_freqs.append(value) # If the value doesn't exist inside the list of freqencies, we add it to it.
    if len(unique_freqs) > 1: # Checking if the list of frequencies has more than one elements. 
        # If there is only one element, there is no MODE, as that implies that all the elements of the list have the same number of occurences.
        max_freq = max(unique_freqs) # We store the larges frequency in a variable 'max_freq'. This is the value of our mode(s).
        for key in grades_dic: # We iterate thorugh the dictionary again to retrieve all the grades that have the same value as 'max_freq'.
            if grades_dic[key] == max_freq: # Checking if the current key in the dictionary hase the same value as 'max_freq'.
                modes.append(key) # If so, the key (grade) is stored inside the list of modes.
    return modes # Returning the MODE(s).

def get_skew(grades_list, mean, median): # This method is used to get the skewness of the grades.
    # To find the skewness, we first need to calculate the standard deviation.
    # To do so, we first need to find the sum of all the squares of the differences between the elements of the list and the MEAN.
    sum_of_difs = 0 # Initiating a variable for the sum of all differences.
    for num in grades_list: # Iterating through the list of grades.
        sum_of_difs += pow(num - mean, 2) # Adding to the sum, the square of the difference between the current grade and the MEAN.
    # To find the standard deviation, we need to take the square root of the division between the sum of all squared differences, and the MEAN.
    stan_div = pow(sum_of_difs/len(grades_list), 1/2) # Getting the square root of a number is the same as raising that number to 1/2.
    # To get the skewness, we need to subtract the MEAN by the MEDIAN and multiply the result my 3, then deviding it by the stantard deviation.
    skew = (3*(mean-median))/stan_div 
    return skew # Returning the skewness.

def get_main_menu(grades_list): # This method is used to get the main menu.
    while True: # Starting an indefinite loop, because the user can choose when to exit the program, in which case we'll break out of the loop.
        print("1. Get the MEAN.") # Printing the option to get the MEAN.
        print("2. Get the MEDIAN.") # Printing the option to get the MEDIAN.
        print("3. Get the MODE.") # Printing the option to get the MODE.
        print("4. Get the SKEWNESS.") # Printing the option to get the SKEWNESS.   
        print("5. Display the list of grades.") # Printing the option to get display the list of grades
        print("6. Add more grades to list.") # Priting the option to add more grades to the list.
        print("Enter q to quit...") # Printing the option to quit the program.
        choice = input(">>> Choice: ") # Taking the user's choice, and storing it into a variable 'choice'.
        print("******************************************")# Adding a separation line.
        if choice == '1': # Checking if the user chose option 1.
            print(">>> The MEAN is:", get_mean(grades_list)) # Printing the MEAN. To do so we call the get_mean function.
            print("******************************************")# Adding a separation line.
        elif choice == '2': # Checking if the user chose option 2.
            print(">>> The MEDIAN is:", get_median(grades_list)) # Printing the MEDIAN. To do so we call the get_median function. 
            print("******************************************")# Adding a separation line.
        elif choice == '3': # Checking if the user chose option 3.
            modes = get_mode(grades_list) # Retrieving the MODE(s) by calling the get_mode function.
            if len(modes) == 0: # Checking if the length of the list is equal to 0, which means that the list is empty and there is no mode.
                print(">>> There is no MODE.") # Printing to the screen that there is no MODE.
                print("******************************************")# Adding a separation line.
            elif len(modes) == 1: # Checking if the lenght of the list is equal to 1, which means there is one MODE.
                print(">>> The MODE is:", modes[0]) # Printing the MODE to the screen.
                print("******************************************")# Adding a separation line.
            else: # If there's more than one mode, the following code is executed.
                print(">>> The MODES are:", *modes) # Printing the modes to the screen.
                print("******************************************")# Adding a separation line.
        elif choice == '4': # Checking if the user chose option 4.
            # Printing the SKEWNESS, by calling the get_skew function, along with the get_mean and get_median functions as parameters.
            print(">>> The SKEWNESS is:", get_skew(grades_list, get_mean(grades_list), get_median(grades_list)))
            print("******************************************")# Adding a separation line.
        elif choice == '5': # Checking if the user chose option 5.
            sorted_list = sorted(grades_list) # Sorting the list of grades for a more readable result, using the sorted function.
            print(">>> Grades", sorted_list) # Printing the sorted list to the screen.
            print("******************************************")# Adding a separation line.
        elif choice == '6': # Checking if the user chose option 6.
            add_number_to_list(grades_list) # Calling the add_number_to_list function.
        elif choice == 'q': # Checking if the user chose option 7.
            with open("grades.txt", 'w+') as file: # Trying to open the file 'grades.txt' with 'w+, so that if there already is a file with that name,
                # it would get overwritten. This is to make sure that in case the file gets temperd with during the running of the program, it gets fixed
                # at the end. 'w+' is also used to make sure that in case the file didn't exist at the beginning of the program or in case the file gets
                # deleted during the running of the program, a new file would be created.
                file.write("Grades: ") # Overwriting whatever was written inside the file already, and prepering it by writing 'Grades: ' which is going
                # to be followed by the list of numbers. If the file already existed at the beginning of the program, its contents would've already be stored
                # inside of grades_list, meaning that there is no problem with overwritting it. If the file doesn't exist, a new one with the same name would be created.
            with open("grades.txt", 'a') as file: # Now that the file is prepared, we open it again but this time using 'a', so that 'Grades: ' doesn't get 
                # overwritten, but also as we iterate through the list to write each grade individually, they don't end up overwriting each other.
                grades_list.sort() # Making sure the list is sorted so that the file looks more organised.
                for index, num in enumerate(grades_list): # Iterating through the list using the 'enumerate' function, so that we can keep track of the index
                    # of each element of the list.
                    if index == len(grades_list) - 1: # Checks if the index is the same as the lenght of the list minus 1, indicating that its the last element.
                        file.write(str(num) + ';') # Writing the last element and a ';' after.
                    else:
                        file.write(str(num) + ',') # Writing all other elements and a ',' after.
            break # Breaking out of the loop, and therefor quiting the program.
        else: # In the user inputs anything else other than the options provided, the following code will execute.
            print(">>>", choice, "is not an option!") # Printing an error message.
            print("******************************************")# Adding a separation line.

def main(): # The main method is executed the run the program.
    grades_list = [] # Initiating the list of grades. 
    read_file(grades_list) # Calling the 'read_file' function which will try to read the data from a file and populate the list with whatever valid numbers it can find.
    # If no such file exists or if there is no valid number to retrieve, the list of grades would remain empty.
    print("******************************************")# Adding a separation line.
    if len(grades_list) < 2: # Checking if there are at least 2 elements inside of grades_list after trying to read the file.
        add_number_to_list(grades_list) # If there aren't enough numbers, the 'add_number_to_list' to make the user have to input them manually.
    get_main_menu(grades_list) # At this point, there should be at least 2 elements inside the list, so the user can proceed to the main menu.
    
    
main()
