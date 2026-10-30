# وارد کردن تابع تبدیل اعداد به حروف از ماژول persian_tools
from persian_tools import digits

# لیست دروس ارائه شده توسط دانشگاه
offered_courses = [{'name': 'python', 'unit': 3, 'teacher': 'sara'},
                   {'name': 'java', 'unit': 2, 'teacher': 'amir'},
                   {'name': 'c#', 'unit': 5, 'teacher': 'zahra'},
                   {'name': 'c++', 'unit': 5, 'teacher': 'mohsen'},
                   {'name': 'python', 'unit': 3, 'teacher': 'ahmad'}
                   ]
# لیست دروس درخواستی دانشجو
student_1 = {'name': 'python', 'unit': 5, 'teacher': 'marjan'}
student_2 = {'name': 'python', 'unit': 3, 'teacher': 'ahmad'}
student_3 = {'name': 'java', 'unit': 2, 'teacher': 'amir'}
student_4 = {'name': 'c#', 'unit': 5, 'teacher': 'zahra'}
student_5 = {'name': 'java', 'unit': 3, 'teacher': 'amir'}
selected_courses = [student_1, student_2, student_3, student_4, student_5]

# -------------------------------------------------------------------------------------------

# بررسی تطابق دروس درخواستی دانشجو با دروس ارائه شده
matched_courses = list(filter(lambda course: course in offered_courses, selected_courses))

print('Matched courses:')
for course in matched_courses:
    print(f"Name={course['name']:8}/Unit={course['unit']:<3}/Teacher={course['teacher']:10}")

matched_count = len(matched_courses)
print('Matched courses count:', matched_count)

# -----------------------------------------------------------------------------------------

# مرتب سازی تعداد دروس به ترتیب صعودی
sorted_units = sorted(list(map(lambda course: course['unit'], matched_courses)))
print('Sorted By Unit:', sorted_units)

# -----------------------------------------------------------

# مرتب سازی نام دروس بر اساس حروف الفبا
sorted_course_names = sorted(list(map(lambda course: course['name'], matched_courses)))
print('Courses Sorted Alphabetically:', sorted_course_names)


# -------------------------------------------------------------------
# تعیین شهریه هر درس بر اساس تعداد واحد آن درس
def add_unit_price(course):
    if course['unit'] == 2:
        course['price'] = 1000
    elif course['unit'] == 3:
        course['price'] = 1200
    elif course['unit'] == 5:
        course['price'] = 1400
    return course


courses_with_fees = list(map(add_unit_price, matched_courses))

# ----------------------------------------------------------------------

# استخراج شهریه دروس و محاسبه مجموع هزینه ها
course_fees = list(map(lambda course: course['price'], matched_courses))
print('Course List:', course_fees)

total_tuition = sum(course_fees)
print('Total Tuition:', total_tuition)

# ----------------------------------------------------------------------

# تبدیل مبلغ کل شهریه به حروف
print('Total Tuition in Words:', digits.convert_to_word(total_tuition))