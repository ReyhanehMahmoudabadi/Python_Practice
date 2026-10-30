from lesson import Lesson

# tested
# ایجاد شئ اول از کلاس Lesson
lesson_1 = Lesson()

# مقدار دهی ویژگی های کلاس اول
lesson_1.code = 3353
lesson_1.name = 'math'
lesson_1.teacher = 'amiri'

# ذخیره اطلاعات و تغییر و نمایش مشخصات خودروی اول
print(lesson_1.save())
print(lesson_1.edit())
print(lesson_1)

print('-------------------------------------------')

# tested
# ایجاد شئ اول از کلاس Lesson
lesson_2 = Lesson()

# مقدار دهی ویژگی های کلاس دوم
lesson_2.code = 126
lesson_2.name = 'chem'
lesson_2.teacher = 'akbari'

# ذخیره اطلاعات و تغییر و نمایش مشخصات خودروی اول
print(lesson_2.save())
print(lesson_2.edit())
print(lesson_2)