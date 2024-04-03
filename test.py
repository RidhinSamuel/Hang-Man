class AreaCalculator:
    def __init__(self) -> None:
        pass
    def area(self,a,b):
        return a*b
    def area(self,a):
        return a*a
sq=AreaCalculator()
print("area of square is", sq.area(4))
print("area of square is", sq.area(4,3))

