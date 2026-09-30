# چاپ اعداد زوج بین1 تا 100 بخش پذیر بر 7
numbers = []

# بررسی اعداد زوج بین 1 تا 100
for num in range(2, 100, 2):
    # بررسی بخش پذیری عدد بر 7
    if num % 7 == 0:
        # اضافه کردن عدد مورد نظر به لیست
        numbers.append(num)

# چاپ لیست اعداد مورد نظر
print('Even numbers divisible by 7:', numbers)