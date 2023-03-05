def collatz(number):
    if number % 2 == 0:
        number2 = number // 2
        print(number2)
        return number2
    elif number % 2 != 0:
        number2 = 3 * number + 1
        print(number2)
        return number2

if __name__ == '__main__':
    while True:
        try:
            number = int(input("Wählen Sie eine positve ganze Zahl: "))
        except ValueError:
            print("Sie haben keinen gültigen Wert eingegeben!")
            continue

        if number > 0:
            number = collatz(number)
            while number != 1:
                number = collatz(number)
        else:
            print("Sie haben keinen gültigen Wert eingegeben ")