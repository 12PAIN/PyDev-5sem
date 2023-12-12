class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError('Ширина или высота отрицательны')

        elif not isinstance(height, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError('Введенные данные имеют не числовой тип.')

        else:
            self.h = height
            self.w = width

    def get_area(self) -> int:
        return self.w * self.h

    def get_perimetr(self) -> int:
        return (self.w + self.h) * 2
