# لیست نگهداری اطلاعات ماشین های پارکینگ
parking_list = []


# نمایش منو اصلی و دریافت انتخاب کاربر
def show_menu():
    print('1)Enter to parking')
    print('2)Parking list')
    print('3)Search car by plate')
    print('4)Exit')
    option = int(input('Enter your choice:'))
    return option


# دریافت اطلاعات ماشین از کاربر و برگرداندن آن به صورت دیکشنری
def get_car_information():
    name = input('Enter car name:')
    color = input('Enter car color:')
    plate = input('Enter car plate:').strip()
    enter_time = input('Enter car enter_time:')
    return {
        "name": name,
        "color": color,
        "plate": plate,
        "enter_time": enter_time
    }


# نمایش اطلاعات تمام ماشین‌های ثبت شده در پارکینگ
def print_parking_list(parking_list):
    print('Parking list:')
    if not parking_list:
        print('The parking lot is empty.')
        return
    for car in parking_list:
        print(f"{car['name']:10} {car['color']:10} {car['plate']:10} {car['enter_time']:10}")


# جستجو‌ی ماشین بر اساس پلاک و برگرداندن آن
def find_car_by_plate(parking_list, plate):
    plate = plate.strip()
    for car in parking_list:
        if car['plate'].lower() == plate.lower():
            return car
    return None
