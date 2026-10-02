# برنامه دریافت درس تا زمانی که جمع واحدها به 17 واحد برسد
lesson_list = []
count_unit = 0

# حلقه دریافت اطلاعات درس
while True:
    title = input('Enter the title:')
    teacher = input('Enter the teacher:')
    duration = int(input('Enter the duration:'))
    unit = int(input('Enter the unit:'))

    # بررسی اینکه مجموع واحدها از 17 بیشتر نشود
    if count_unit + unit > 17:
        break

    # اضافه کردن واحد به مجموع واحدها
    count_unit += unit

    # اضافه کردن اطلاعات درس به لیست در قالب دیکشنری
    lesson = {'title': title, 'teacher': teacher, 'duration': duration, 'unit': unit}
    lesson_list.append(lesson)
    print('Saved!!!')

    # پایان حلقه در صورت رسیدن مجموع واحدها به 17
    if count_unit == 17:
        break

# نمایش لیست نهایی دروس
for lesson in lesson_list:
    print(
        f"Title={lesson['title']:10}|Teacher={lesson['teacher']:10}|Duration={lesson['duration']:2}|Unit={lesson['unit']:2}")
