# تعریف کلاس خودرو
class Car:

    # مقدار‌دهی اولیه ویژگی‌های خودرو
    def __init__(self):
        self.name = None
        self.color = None
        self.plate = None

    # ایجاد پیام تایید ذخیره اطلاعات خودرو
    def save(self):
        return f"Saved : {self.name} {self.color} {self.plate}"

    # تغییر پلاک خودرو
    def change_plate(self):
        print('Change plate')

    # تعیین نحوه نمایش اطلاعات شئ
    def __repr__(self):
        return f"Name={self.name} / Color={self.color} / Plate={self.plate}"
