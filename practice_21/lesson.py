# تعریف کلاس درس
class Lesson:
    # مقداردهی اولیه ویژگی‌های درس
    def __init__(self, code, name, teacher):
        self.code = code
        self.name = name
        self.teacher = teacher

        print('------------------')

    # ------------------------------------------

    # تعریف Property برای دسترسی به کد درس
    @property
    def code(self):
        return self.__code

    # اعتبارسنجی و مقداردهی کد درس
    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError('Code must be of type int')
        self.__code = code

    # ---------------------------------------------

    # تعریف Property برای دسترسی به نام درس
    @property
    def name(self):
        return self.__name

    # اعتبارسنجی و مقداردهی نام درس
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be of type str')
        self.__name = name

    # -----------------------------------------------

    # تعریف Property برای دسترسی به نام استاد
    @property
    def teacher(self):
        return self.__teacher

    # اعتبارسنجی و مقداردهی نام استاد
    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, str):
            raise TypeError('Teacher must be of type str')
        self.__teacher = teacher

    # --------------------------------------------------

    # تعیین نحوه نمایش اطلاعات درس
    def __repr__(self):
        return f"SAVED: Lesson code={self.code} | Lesson name={self.name} | Teacher name={self.teacher}"