result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 11: 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except NameError as error:
        print("Помилка імені:", error)
    except ValueError as error:
        print("Помилка значення (ValueError):", error)
    except IndexError as error:
        print("Помилка індексу (IndexError):", error)
    except ZeroDivisionError as error:
        print("Ділення на нуль:", error)
    except TypeError as error:
        print("Помилка типу даних (TypeError):", error)

print("Результат:", result)