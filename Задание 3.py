def isfib(number):
    num1 = 1
    num2 = 1
    while True:
        if num2 <= number:
            if num2 == number:
                print('YES')
                break
            else:
                tempnum = num2
                num2 += num1
                num1 = tempnum
                
        else:
            print('NO')
            break
                
print(isfib(int(input())))
#программа скопирована из интернета потому что я не умею писать программы)
