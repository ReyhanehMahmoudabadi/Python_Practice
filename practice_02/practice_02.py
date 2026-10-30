# بررسی امکان دریافت مجوز ساخت بر اساس مساحت زمین

# اطلاعات زمین
length = int(input('Enter the length:'))
width = int(input('Enter the width:'))

# محاسبه مساحت زمین
area = length * width

# چاپ مساحت زمین
print('Area:', area)

# بررسی امکان دریافت مجوز
match area:
    case _ if 0 < area <= 100:
        print('این مقدار مساحت، نیاز به دریافت مجوز ندارد.')
    case _ if 100 < area <= 200:
        print('این مقدار مساحت، نیازمند دریافت مجوز است.')
    case _ if 200 < area:
        print('به این مقدار مساحت، مجوز صادر نمی گردد.')
    case _:
        print('مساحت وارد شده معتبر نیست!')
