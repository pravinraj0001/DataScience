"""Registration and Login system using Python, file handling
"""
'''Verifying the login details'''


def userPage(username):
    print("#" * 100)
    print(f"{' User Page ':#^100}")
    print("")
    print(f"{' WELCOME TO USER PAGE ':^100}")
    print(f"{username:^100}")
    print(f"{' YOU ARE SUCCESSFULLY LOGGED IN ':^100}")
    print("")
    print("#" * 100)
    return input("Press '1' for EXIT : ")

def fileread(username, password):
    file = open('userdetails.txt', 'r')
    Lines = file.readlines()
    print(Lines)
    for line in Lines:
        if username in line:
            if password in line.split(",")[1]:
                s = ''
                while(s != '1'):
                    s = userPage(username)
                return '3'
        else:
            print("Invalid username or password!! Please try again.")
            return '1'

def login():
    '''Login page'''
    print("#" * 100)
    print(f"{' Login Page ':#^100}")
    print("")
    username = input("Username : ")
    password = input("Password: ")
    print("")
    print("#" * 100)
    return fileread(username, password)

def userValid(username):
    if '@' in username and '.' in username:
        p,q = username.index('@'), username.index('.')
        if p < q and username[q-1].isalpha() and username[q+1].isalpha() and username[p-1].isalpha():
            return True
    else:
        print("Invalid username!! Please enter again")
        return False

def passValid(password):
    l = int(len(password))
    v = ''
    if 5 < l < 16:
        for i in password:
            if 21 <= int(ord(i)) <= 47 or 58 <= int(ord(i)) <= 64:
                v += 's'
            if i.isupper():
                v += 'u'
            if i.islower():
                v += 'l'
            if i.isdigit():
                v += 'd'

    if 's' in v and 'u' in v  and 'l' in v and 'd' in v:
        return True
    else:
        print("Invalid password!! Please enter again")
        return False

def registeration():
    file = open('userdetails.txt', 'a')
    '''Registration page'''
    print("#"*100)
    print(f"{' Registration Page ':#^100}")
    print("")
    username = input("Username : ")
    password = input("Password: ")
    print("")
    print("#"*100)

    if userValid(username) and passValid(password):
        print("Saved in file")
        file.write(username+","+password+"\n")
        file.close()
        return '1'
    else:
        return '2'


if __name__ == '__main__':
    file = open('userdetails.txt', 'w')
    file.close()
    choice = ''
    while (choice != '3'):
        print(f"{'Registration From':#^100}")
        choice = input("\nPlease select on the below form: \n\t1) Login\n\t2) Registration\n\t3) Exit\n")
        if choice == '1':
            choice = login()
            continue
        elif choice == '2':
            choice = registeration()
            continue
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid Choice")
        print("#" * 100)


