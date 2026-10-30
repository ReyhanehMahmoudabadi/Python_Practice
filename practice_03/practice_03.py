# برنامه چاپ قرینه عدد وارد شده تا خود عدد

# دریافت عدد
try:
    number = int(input('Enter the number:'))
    # بررسی مقدار عدد
    match number:

        case _ if number == 0:
            print('Number is zero!!!')

        # چاپ اعداد از قرینه تا خود عدد
        case _ if number > 0:
            for i in range(-number, number + 1, 1):
                print(i)

        # چاپ اعداد از قریته نا خود عدد
        case _ if number < 0:
            for i in range(-number, number - 1, -1):
                print(i)

# نمایش خطا برای ورودی غیر صحیح
except ValueError:
    print('Please enter an integer!!!')