def password_to_list(password):
    password_list = []

    for char in password:
        password_list.append(ord(char) - 96)

    return password_list

def list_to_password(password_list):
    password = ""

    for num in password_list:
        password += chr(num+96)

    return password

def increment(index, password_list):
    password_list[index] += 1
    if password_list[index] > 26:
        password_list[index] = password_list[index]%26
        increment(index-1, password_list)

def increment_password(password):
    password_list = password_to_list(password)

    increment(len(password_list)-1, password_list)

    password = list_to_password(password_list)

    return password

def is_consecutive(list):
    if list[1] - list[0] == list[2] - list[1] == 1:
        return True
    else:
        return False

def req1(password):
    password_list = password_to_list(password)
    for i in range(len(password_list)-2):
        if is_consecutive(password_list[i:i+3]):
            return True
    return False

def req2(password):
    if any(i in password for i in ['i', 'o', 'l']):
        return False
    else:
        return True

def req3(password):
    indices = []

    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            indices.append(i)

    if len(indices) > 1 and max(indices) - min(indices) > 1:
        return True
    else:
        return False


password = "hepxcrrq"
while True:
    password = increment_password(password)
    if req1(password) and req2(password) and req3(password):
        print(f"Part 1: {password}")
        break

while True:
    password = increment_password(password)
    if req1(password) and req2(password) and req3(password):
        print(f"Part 2: {password}")
        break


