import loguru
class People:
    def __init__(self,dr):
        self.driver = dr

class student(People):
    def __init__(self,dr):
        super().__init__(dr)

xiaoming = student('brwoser')

print( xiaoming.driver )

