# برناه محاسبه میانگین اعداد فرد دریافتی
odd_numbers = []

# تشخیص و دریافت اعداد فرد
while True:
    number = int(input("Enter a number:"))
    if number == 0:
        break
    if number % 2 != 0:
        odd_numbers.append(number)

# چاپ لیستی از اعداد فرد دریافتی
print('Odd numbers:', odd_numbers)

# بررسی وجود اعداد فرد
if len(odd_numbers) > 0:
    # محاسبه میانگین
    avg = sum(odd_numbers) / len(odd_numbers)
    # چاپ میانگین
    print(round(avg, 2))

# نمایش پیام در صورت نبودن عدد فرد
else:
    print('No odd number entered!!!')