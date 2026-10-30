# وارد کردن ماژول های مورد نیاز از کتابخانه persian_tools
from persian_tools import plate, national_id, phone_number, bill
from persian_tools.bank import card_number


# نمایش منوی اصلی و دریافت انتخاب کاربر
def show_menu():
    print("1)Enter a national id")
    print("2)Enter a phone number")
    print("3)Enter a card number")
    print("4)Enter a car plate")
    print("5)Enter a bill id")
    print("0)Exit")
    option = int(input("Enter your choice:"))
    return option


# بررسی اعتبار کد ملی و دریافت اطلاعات محل صدور
def check_national_id(id_number):
    if not national_id.validate(id_number):
        raise ValueError('Invalid national id!')
    return national_id.find_place(id_number)


# بررسی اعتبار شماره موبایل و دریافت اطلاعات اپراتور
def check_phone_number(phone):
    if not phone_number.validate(phone):
        raise ValueError('Invalid phone number!')
    return phone_number.operator_data(phone)


# بررسی اعتبار شماره کارت بانکی و دریافت اطلاعات بانک
def check_card_number(card):
    if not card_number.validate(card):
        raise ValueError('Invalid card number!')
    return card_number.bank_data(card)


# بررسی اعتبار شماره پلاک و دریافت اطلاعات خودرو
def check_car_plate(car_plate):
    if not plate.is_valid(car_plate):
        raise ValueError('Invalid car plate!')
    return plate.get_info(car_plate)


# بررسی اعتبار شناسه قبض و شناسه پرداخت و دریافت اطلاعات قبض
def check_bill_id(bill_number, payment_number):
    result = bill.get_detail(bill_number, payment_number)

    if not result:
        raise ValueError('Invalid bill information!')
    return result