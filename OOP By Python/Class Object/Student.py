class Student:
    def __init__(self,name,magor,gpa):
        self.name = name
        self.magor = magor
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= str(3.5):
            return True
        else:
            return False