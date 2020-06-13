# прораммын алдаа олох, эсвэл алдаа гарах магадлалтай үед энд бичнэ.
try:
    print(x)
except NameError as error :
    print(error)
finally:
    pass
prnt(15)


print('-' *30)


def add_list(numbers:list , number: int = -999):
    try:
        numbers.append(number)
    except AttributeError:
        numbers = []
        numbers.append(number)
    except Exception:  # бүх төрлийн алдаа барих
        numbers = []
        numbers.append(number)

    return numbers

    
nums= [1,2,3]
new = add_list(15,4)
print(new)
