class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        

    def configuration(self):
        print("Configuration is : ",self.cpu, self.ram)

com1 = Computer("i5",16)
com2 = Computer("hp",4)

com1.configuration()
com2.configuration()

