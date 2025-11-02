#batch program that generates a file of username assignments from a file of names

#two files have been provided as starter files
    #employee_names.txt
    #empty_file.txt

#prompt the user for the name of the input file


start_file = input("Please enter the name of the file containing names: ")

#for each text line in the input file:
    #extract the first and last name
    #create a username using the first letter of the first name combined with the first
    #seven letters of the last name (all in lower case)
usernames_file = open("username_assignments.txt", "w+") #open username file in write+ mode
name_file = open(start_file, "rt") #open name file given by user in read mode
names = name_file.read() #read the files to string names

#using strings names isolate first letter of first name, and first 7 of last name (lowercase)
name_list = names.split("\n") #make the string of names a list
with open(start_file, 'r') as file_obj:
    first_char = file_obj.read(1)
    if not first_char:
        print(f'0 lines were processed from input file: {start_file}')
        print(f'Created username assignments file as: username_assignments.txt')
    else:
        for i in range(0, len(name_list)-1):
            sep_names = name_list[i].split() #make the first and last names separate in the list
            name_tog = sep_names[0] + sep_names[1] #combine first and last names
            lower_name = name_tog.lower() #combined names lowercase
            last = sep_names[1] #assign last name
            last_name = last[:7] #assign last name but max 7 letters
            username_full = lower_name[0] + last_name #combines first let of first name to lastname

            username_lower = username_full.lower() #full username in lowercase

            #write a line to the output file with the following format
                #FirstName LastName,username
            usernames_file.write(f'{str(sep_names[0])} {str(sep_names[1])}, {username_lower} \n ')

            #at the conclusion of the program, print the total number of text lines processed from
            #the input file

        print(f'{len(name_list)} lines were processed from input file: {start_file}')
        print(f'Created username assignments file as: username_assignments.txt')
