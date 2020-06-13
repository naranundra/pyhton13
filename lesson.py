# нэг класс нөгөө класс даа удамших, классын гишүүн өгөгдөл
# болон функцыг өвлөн авна
class Person: # том үсгээр эхэлнэ
    def __init__(self, name: str, nas: int):
        self.__name = name
        self.__nas = nas 
    def say_hi(self):
        print("Hi i am", self.__name, self.__nas)

class Student(Person):
    def __init__(self, ner, nas, code):
        super().__init__(ner, nas)
        self.code = code 

class Job(Person):
    def __init__(self, ner, nas, mergejil):
        super().__init__(ner, nas)
        self.mergejil = mergejil

   
# super().__init__()  эх классаас функыг дуудах үед энэ функцыг ашиглаад
# удамшуулж болно 

s2 = Job('Turuu', 40, 'Teacher')
s2.say_hi() 
print(s2.mergejil)