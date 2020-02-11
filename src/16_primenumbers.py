
num = input("Enter a number: ")

try:
    int(num)
    int_num = int(num)
    if int_num > 1:
        for n in range(2, int_num):
            if (int_num % n) == 0:
                print(f'{num} is not a prime number')
                break
            else:
                print(num, 'is a prime number')
                break
    else:
        print(num, 'is not a prime number')
except ValueError:
    try:
        float(num)
        print(num, 'is not a prime number')
    except ValueError:
        print('Input cannot be a string!')
            