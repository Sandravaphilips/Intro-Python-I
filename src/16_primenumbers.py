
# num = input("Enter a number: ")

# try:
#     int(num)
#     int_num = int(num)
#     if int_num > 1:
#         for n in range(2, int_num):
#             if (int_num % n) == 0:
#                 print(f'{num} is not a prime number')
#                 break
#             else:
#                 print(num, 'is a prime number')
#                 break
#     else:
#         print(num, 'is not a prime number')
# except ValueError:
#     try:
#         float(num)
#         print(num, 'is not a prime number')
#     except ValueError:
#         print('Input cannot be a string!')
            
import math
n = int(input("Enter number: "))
sqrt_n = math.floor( math.sqrt(n))

n_array = [i for i in range(2, n+1)]
   
for i in range(2, sqrt_n + 1):
    if i:
        for x in range(n):
            j = i**2 + i*x
            while j <= n:
                if j in n_array:
                    n_array[n_array.index(j)] = False
                break

for y in n_array:
    if y :
        print(y)