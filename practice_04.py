# محاسبه ی میانگین اعداد زوج سه رقمی بخش پذیر بر هفت

# تعریف متغیرهای مجموع و تعداد اعداد
sum_even_num = 0
count_even_num = 0

print('Three-digit even numbers divisible by seven:')
# بررسی اعداد زوج سه رقمی
for i in range(100, 999, 2):
    # بررسی بخش پذیری عدد بر هفت
    if i % 7 == 0:
        sum_even_num += i
        count_even_num += 1
        print(i)

# محاسبه میانگین
avg = sum_even_num / count_even_num
# چاپ میانگین
print('Average of three-digit even numbers divisible by seven:', avg)