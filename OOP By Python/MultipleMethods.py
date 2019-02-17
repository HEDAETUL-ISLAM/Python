class Student:

    
    def __init__(self,v1,v2,v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3

    def avg(self):
        return (self.v1+self.v2+self.v3)/3

    

    # def get_v1(self):
    #     return self.v1
                                    #these getter setters are called mutater
    # def set_v1(self,v1):
    #     self.v1=v1

s1=Student(1,2,3)
s2=Student(4,5,6)

print(s1.avg())

print(s2.avg())


