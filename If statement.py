
'''

class Array:
    student = 0
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        Array.student += 1

    def showcount(self):
        print("Total student:"+ str(Array.student))

stu = Array(90,85)
stu = Array("Raju", 90)
stu.showcount()


Weight:
