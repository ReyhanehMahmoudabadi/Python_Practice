# وارد کردن توابع مورد نیاز از ماژول
from validate_module import *

# اجرای مداوم برنامه تا زمان انتخاب گزینه خروج
while True:

    # اجرای دستورات برنامه و بررسی خطاهای احتمالی
    try:
        option = show_menu()
        print("----------------------------------")

        match option:

            # بررسی کد ملی
            case 1:
                id_number = input("Enter a national id: ")
                result = check_national_id(id_number)
                print("National id is valid!")
                print("Place information:", result)

            # بررسی شماره موبایل
            case 2:
                phone = input("Enter your phone number: ")
                result = check_phone_number(phone)
                print("Phone number is valid!")
                print("Operator information:", result)

            # بررسی شماره کارت بانکی
            case 3:
                card = input("Enter your card number: ")
                result = check_card_number(card)
                print("Card number is valid!")
                print("Bank information:", result)

            # بررسی شماره پلاک خودرو
            case 4:
                car_plate = input("Enter your car plate: ")
                result = check_car_plate(car_plate)
                print("Car plate is valid!")
                print("Car information:", result)

            # بررسی شناسه قبض و شناسه پرداخت
            case 5:
                bill_number = input("Enter your bill id: ")
                payment_number = input("Enter your payment id: ")
                result = check_bill_id(bill_number, payment_number)
                print("Bill information:", result)

            # خروج از برنامه
            case 0:
                break

            # مدیریت انتخاب‌های نامعتبر
            case _:
                print("Error: Invalid choice!")

    # مدیریت خطاهای احتمالی برنامه
    except ValueError:
        print("Error! Please try again!")

    print("----------------------------------")