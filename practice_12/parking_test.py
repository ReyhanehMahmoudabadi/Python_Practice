# from parking_module import *


# تست اول: بررسی عملکرد منوی اصلی
# test passed
# p = show_menu()
# print(p)


# تست دوم: بررسی دریافت اطلاعات ماشین
# test passed
# information = get_car_information()
# print(information)


# تست سوم: بررسی نمایش لیست پارکینگ
# test passed
# sample_list = [
#     {'name': 'benz', 'color': 'red', 'plate': '12p44', 'enter_time': '14:25'},
#     {'name': 'bmw', 'color': 'black', 'plate': '74l55', 'enter_time': '6:22'},
#     {'name': 'GMC', 'color': 'black', 'plate': '11R14', 'enter_time': '21:55'}
# ]
# print_parking_list(sample_list)


# تست چهارم: بررسی پیدا کردن ماشین با پلاک موجود
# test passed
# f = find_car_by_plate(sample_list, '11R14')
# print(f)


# تست پنجم: بررسی جستجوی پلاک ناموجود
# test passed
# f = find_car_by_plate(sample_list, '99A99')
# print(f)