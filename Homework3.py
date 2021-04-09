#Task1
class MyList(object):
    def __init__(self, data):
        self.data = data

    def __mul__(self, other):
        return self.data * other

    def __add__(self, other):
        return self.data + other.data

    def __str__(self):
        return str(self.data)

l1 = MyList([1,2,3,4])
l2 = MyList([5,6,7])
print(l1.data)
print(l1 * 2)
print(l1 + l2)
print(str(l1))


#Task2
class TestPaper:
    def __init__(self, subject, mark_scheme, pass_mark):
        self.subject = subject
        self.mark_scheme = mark_scheme
        self.pass_mark = pass_mark

class Student:
    def __init__(self):
        self.tests_taken = {}
        self.grade = '0%'
        self.pass_status = ''
        self.subject = ''

    def Tests_taken(self):
        if self.tests_taken == {}:
            print("No Tests Taken!")
        else:
            print(self.tests_taken)

    def take_test(self, other, studAnswers):
        try:
            correctAnswers = 0
            for i in range(0, len(other.mark_scheme)):
                if studAnswers[i] == other.mark_scheme[i]:
                    correctAnswers += 1
            self.subject = other.subject
            self.grade = str(correctAnswers/len(other.mark_scheme)*100) + '%'
            if str(correctAnswers/len(other.pass_mark)*100)+'%' >= other.pass_mark:
                self.pass_status = "Failed!"
            else:
                self.pass_status = "Passed!"
            self.tests_taken.update({other.subject:self.pass_status})
        except AttributeError:
            print("Wrong Input Detected!")




test1 = TestPaper("Math", ["1A","2C","3D","4C"], "41%")
test2 = TestPaper("Chemistry", ["1A","2B","3C","4D","5A","6B","7C","8D"], "50%")

student1 = Student()
student1.Tests_taken()
student1.take_test(test1, ["1A","2B","3D","4C"])
student1.Tests_taken()
student1.take_test(test2, ["1A","2C","3C","4D","5B","6B","7C","8D","9A"]) #Purposfully Made answer String Bigger; still works :D
student1.Tests_taken()