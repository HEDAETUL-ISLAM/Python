class Vector2D:
    x=0
    y=0

    def Set(self, x, y):
        self.x = x
        self.y = y

def Main():
    vector = Vector2D()
    vector.Set(5,6)
    print("X: "+str(vector.x)+" Y: "+str(vector.y))

Main()