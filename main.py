#1
# try:
#     a = int(input('Write first number: '))
#     b = int(input('Write second number: '))
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("Chislo ne delitsya na nol")


#2
# try:
#     file = True
#     if file:
#         with open('example.txt', 'r') as open:
#             content = open.read(file)
#             print('your file is', content)
#     else:
#         print('file is empty')
# except FileNotFoundError:
#     print('file not found')
#3
# try:
#     a = int(input("Enter int number:"))
#     b = a / 100
#     print("Your answer is", b)
# except ZeroDivisionError:
#     print("you entered schose 0")
# except ValueError:
#     print("you entered string ")
# 4 
# try:
#     file = "hello"
   
#     with open('example.txt', 'w') as open:
#               content = open.write(file)
#               print("your file is", content)

# except FileNotFoundError:
#     print("file not found")

5
# try:
#     a = input("Введите число: ")
#     b = int(a)
# except ValueError:
#     print("Это не целое число!")
# else:
#     print(f"Вы ввели число {b}.")
# finally:
#     print("Программа завершена.")