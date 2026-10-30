# تعریف کلاس درس
class Lesson:

    # مقداردهی اولیه ویژگی‌های کلاس
    def __init__(self):
        self.code = None
        self.name = None
        self.teacher = None

    # ایجاد پیام تایید ذخیره اطلاعات کلاس
    def save(self):
        return f"SAVE : {self.code} {self.name} {self.teacher}"

    # تغییر کلاس
    def edit(self):
        return ('Edited')

    # تعیین نحوه نمایش اطلاعات شئ
    def __repr__(self):
        return f"Lesson code={self.code} / Lesson name={self.name} / Teacher name={self.teacher}"