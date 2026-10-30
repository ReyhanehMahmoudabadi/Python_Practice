# تعریف کلاس خودرو
class Car:
    # مقداردهی اولیه ویژگی‌های خودرو
    def __init__(self, name, color, plate):
        self.name = name
        self.color = color
        self.plate = plate

    # ------------------------------------------------------------
    # تعریف Property برای دسترسی به نام خودرو
    @property
    def name(self):
        return self.__name

    # اعتبارسنجی و مقداردهی نام خودرو
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be of type str')
        self.__name = name

    # -------------------------------------------------------------
    # تعریف Property برای دسترسی به رنگ خودرو
    @property
    def color(self):
        return self.__color

    # اعتبارسنجی و مقداردهی رنگ خودرو
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be of type str')
        self.__color = color

    # -------------------------------------------------------------
    # تعریف Property برای دسترسی به پلاک خودرو
    @property
    def plate(self):
        return self.__plate

    # اعتبارسنجی و مقداردهی پلاک خودرو
    @plate.setter
    def plate(self, plate):
        if not isinstance(plate, str):
            raise TypeError('Plate must be of type str')
        self.__plate = plate

    # ------------------------------------------------------------------
    # تعیین نحوه نمایش اطلاعات خودرو
    def __repr__(self):
        return f"SAVED: Name={self.name} - Color={self.color} - Plate={self.plate}"