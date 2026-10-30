# تعریف کلاس پایه محصولات
class Product:
    # مقداردهی اولیه ویژگی‌های مشترک محصولات
    def __init__(self):
        self.name = None
        self.price = None

    # تعیین نحوه نمایش مشخصات محصول
    def __repr__(self):
        return f"Name={self.name} _ Price={self.price}"


# تعریف کلاس محصولات غیرالکتریکی
class NonElectrical(Product):
    # مقداردهی اولیه ویژگی‌های محصولات غیرالکتریکی
    def __init__(self):
        self.weight = None


# تعریف کلاس مبلمان
class Furniture(NonElectrical):
    # مقداردهی اولیه ویژگی‌های مبلمان
    def __init__(self):
        self.capacity = None
        self.color = None


# تعریف کلاس محصولات الکتریکی
class Electrical(Product):
    # مقداردهی اولیه ویژگی‌های محصولات الکتریکی
    def __init__(self):
        self.voltage = None


# تعریف کلاس لپ‌تاپ
class Laptop(Electrical):
    # مقداردهی اولیه ویژگی‌های لپ‌تاپ
    def __init__(self):
        self.ram = None
        self.cpu = None


# تعریف کلاس تلفن همراه
class Mobile(Electrical):
    # مقداردهی اولیه ویژگی‌های تلفن همراه
    def __init__(self):
        self.display_size = None


# تعریف کلاس گوشی‌های سامسونگ
class Samsung(Mobile):
    # مقداردهی اولیه شماره سریال گوشی
    def __init__(self):
        self.serial = None


# تعریف کلاس گوشی‌های آیفون
class Iphone(Mobile):
    # مقداردهی اولیه شماره سریال گوشی
    def __init__(self):
        self.serial = None