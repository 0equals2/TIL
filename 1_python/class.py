class course:
    name = '4차 4기'

    def introduce(self):
        return self.name

def greeting():
    return 'Hello!'


class Fourth():
    late = '09:10'
    finish = '18:00'
    lunch = '12:10'
    title= 'Deep learning'

class Student(Fourth):
    def set_values(self, name, age):
        self.name = name
        self.age = age

오창희 = Student('오창희', 99)
오창희.set_values('창희', 99)

Student(오창희, '창희', 99) #위와 같은 코드 이지만 위의 코드가 더 적합
