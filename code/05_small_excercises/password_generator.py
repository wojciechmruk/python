import random
import string

password = ''
correct = False
while True and not correct:
    try:
        pass_length = int(input('Pass length:'))
        if pass_length < 5:
            print('Password must be at least 5 characters')
            continue

        lower_case_letters = int(input('How many lower case letters:'))
        if (lower_case_letters > pass_length):
            print(f'Password should be {pass_length} characters long')
            continue

        upper_case_letters = int(input('How many upper case letters:'))
        if (lower_case_letters + upper_case_letters > pass_length):
            print(f'Password should be {pass_length} characters long')
            continue

        numbers = int(input('How many numbers:'))
        if (numbers + lower_case_letters + upper_case_letters > pass_length):
            print(f'Password should be {pass_length} characters long')
            continue

        special = int(input('How many special characters:'))
        if (special + numbers + lower_case_letters + upper_case_letters > pass_length):
            print(f'Password should be {pass_length} characters long')
            continue
        break
    except:
        print('Only numbers!')

for _ in range(pass_length):
    if lower_case_letters > 0:
        password += random.choice(string.ascii_lowercase)
        lower_case_letters -= 1

    if upper_case_letters > 0:
        password += random.choice(string.ascii_uppercase)
        upper_case_letters -= 1

    if numbers > 0:
        password += random.choice(string.digits)
        numbers -= 1

    if special > 0:
        password += random.choice(string.punctuation)
        special -= 1

s = list(password)
random.shuffle(s)

print(''.join(s))
