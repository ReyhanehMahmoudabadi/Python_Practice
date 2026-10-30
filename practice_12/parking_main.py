# وارد کردن توابع و لیست مورد نیاز از ماژول پارکینگ
from parking_module import *

# اجرای مداوم برنامه تا زمان انتخاب گزینه خروج
while True:
    option = show_menu()
    print('--------------------------')

    match option:

        # ثبت ماشین جدید در پارکینگ
        case 1:
            car = get_car_information()
            if find_car_by_plate(parking_list, car['plate']):
                print('This car already registered!!!')
            else:
                parking_list.append(car)
                print('Car registered successfully.')

        # نمایش لیست ماشین‌های پارکینگ
        case 2:
            print_parking_list(parking_list)

        # جستجو‌ی ماشین بر اساس پلاک ماشین
        case 3:
            plate = input('Enter new plate for search:')
            result = find_car_by_plate(parking_list, plate)
            if result:
                print('Car found :', result)
            else:
                print('No car found with this plate number!!!')

        # خروج از برنامه
        case 4:
            break

        # مدیریت انتخاب نامعتبر
        case _:
            print('Error : Invalid Option !!!')

    print('------------------------------------------')
