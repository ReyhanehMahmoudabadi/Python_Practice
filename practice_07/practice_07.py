# برنامه چاپ اعداد زوج و فرد در دو لیست جداگانه

# تعریف لیست های مستقل برای اعداد زوج و اعداد فرد
even_numbers = []
odd_numbers = []

# ایجاد حلقه برای گرفتن اعداد تا زمانی که کاربر 0 وارد نکند
while True:
    number = int(input('Enter the number:'))

    # بررسی عدد که اگر 0 باشد، دریافت عدد متوقف میشود
    if number == 0:
        break

    # بررسی زوج بودن عدد
    if number % 2 == 0:
        even_numbers.append(number)

    # بررسی فرد بودن عدد
    else:
        odd_numbers.append(number)

# چاپ لیست نهایی اعداد زوج و فرد
print('List of even numbers:', even_numbers)
print('List of odd numbers:', odd_numbers)