import math

a = str(input("Введите выражение: "))
print("-" * 150)
n = k = p = t = 0
string_numbers = []
string_symbol = []
num = func = string = ""

for i in range(0, len(a)):
    if a[i] != " ":
        string += a[i]

if string[0] == "-":
    a = "0-"
    n = 1
else:
    a = ""

for i in range(n, len(string)):
    if string[i] == "(" and string[i + 1] == "-":
        a += "(0-"
    elif string[i - 1] == "(" and string[i] == "-":
        continue
    else:
        a += string[i]

string = a
a = ""

for i in range(0, len(string)):

    if string[i] == "^" and string[i + 1] == "(":
        p += 1

    if p > 0 and string[i] == "(":
        t += 1
    elif p > 0 and string[i] == ")":
        t -= 1
        if t == 0:
            p = 0

    if string[i] == "^":
        k += 1
        a += "^("
    elif string[i] in "*/+-" and string[i - 1] != str(0) and p == 0:
        a += ")" * k + string[i]
        k = 0
    else:
        a += string[i]

if k != 0:
    a += ")" * k

print("Обработанное выражение: ", a)
print("-" * 150)

for i in range(0, len(a)):

    if a[i] in "+-*/^()":
        if len(num) != 0:
            string_numbers.append(num)
            num = ""

        if len(func) != 0:
            string_symbol.append(func)
            func = ""

        if len(string_symbol) == 0 or a[i] == "(":
            string_symbol.append(a[i])

        elif a[i] == ")":
            for k in range(len(string_symbol) - 1, -1, -1):
                if string_symbol[k] in "(":
                    string_symbol.pop(k)
                    break
                string_numbers.append(string_symbol.pop())

        elif a[i] == "^":
            for k in range(len(string_symbol) - 1, -1, -1):
                if string_symbol[k] in "(*/+-":
                    string_symbol.append(a[i])
                    break
                else:
                    string_numbers.append(string_symbol.pop())
                    if len(string_symbol) == 0:
                        string_symbol.append(a[i])

        elif a[i] == "*":
            for k in range(len(string_symbol) - 1, -1, -1):
                if string_symbol[k] in "(+-":
                    string_symbol.append(a[i])
                    break
                else:
                    string_numbers.append(string_symbol.pop())
                    if len(string_symbol) == 0:
                        string_symbol.append(a[i])

        elif a[i] == "/":
            for k in range(len(string_symbol) - 1, -1, -1):
                if string_symbol[k] in "(+-":
                    string_symbol.append(a[i])
                    break
                else:
                    string_numbers.append(string_symbol.pop())
                    if len(string_symbol) == 0:
                        string_symbol.append(a[i])

        elif a[i] == "+":
            for k in range(len(string_symbol) - 1, -1, -1):
                if string_symbol[k] in "(":
                    string_symbol.append(a[i])
                    break
                else:
                    string_numbers.append(string_symbol.pop())
                    if len(string_symbol) == 0:
                        string_symbol.append(a[i])

        else:
            for k in range(len(string_symbol) - 1, -1, -1):
                if string_symbol[k] in "(":
                    string_symbol.append(a[i])
                    break
                else:
                    string_numbers.append(string_symbol.pop())
                    if len(string_symbol) == 0:
                        string_symbol.append(a[i])

    elif a[i] in [str(k) for k in range(0, 10)] or a[i] == ".":
        num += a[i]

    else:
        func += a[i]

if len(num) != 0:
    string_numbers.append(num)

for i in range(len(string_symbol) - 1, -1, -1):
    string_numbers.append(string_symbol.pop())

print("Обратная польская нотация: ", string_numbers)
print("-" * 150)

for i in range(0, len(string_numbers)):

    if string_numbers[i] in "^*/+-":
        y = string_symbol.pop()
        x = string_symbol.pop()

        if string_numbers[i] == "^":
            string_symbol.append(x ** y)

        elif string_numbers[i] == "*":
            string_symbol.append(x * y)

        elif string_numbers[i] == "/":
            if y == 0:
                print("ОШИБКА: Деление на ноль")
                exit()
            string_symbol.append(x / y)

        elif string_numbers[i] == "+":
            string_symbol.append(x + y)

        else:
            string_symbol.append(x - y)

    elif string_numbers[i] == "sin":
        string_symbol.append(math.sin(string_symbol.pop()))

    elif string_numbers[i] == "cos":
        string_symbol.append(math.cos(string_symbol.pop()))

    elif string_numbers[i] == "tg":
        x = string_symbol.pop()
        if math.cos(x) == 0:
            print("ОШИБКА: Тангенс не определён, так как косинус равен нулю")
            exit()
        string_symbol.append(math.tan(x))

    elif string_numbers[i] == "ctg":
        x = string_symbol.pop()
        if math.sin(x) == 0:
            print("ОШИБКА: Котангенс не определён, так как синус равен нулю")
            exit()
        string_symbol.append(math.cos(x) / math.sin(x))

    else:
        string_symbol.append(float(string_numbers[i]))

print("Ответ: ", string_symbol[0])
