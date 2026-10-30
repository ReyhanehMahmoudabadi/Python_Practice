# وارد کردن توابع مورد نیاز از ماژول مخاطبین
from contact_module import *

# اجرای مداوم برنامه تا زمان انتخاب گزینه خروج
while True:
    option = show_menu()
    print('----------------------------------')

    match option:

        # افزودن مخاطب جدید به لیست
        case 1:
            contact = get_contact_information()

            # بررسی تکراری نبودن شماره تلفن مخاطب
            if find_contact_by_phone(contact_list, contact['phone']):
                print('Error: This contact already exists!')
            else:
                contact_list.append(contact)
                print('Contact saved successfully!')

        # نمایش لیست مخاطبین
        case 2:
            print_contact_list(contact_list)

        # جستجوی مخاطب بر اساس شماره تلفن
        case 3:
            phone = input('Enter a phone number:')
            result = find_contact_by_phone(contact_list, phone)

            # بررسی نتیجه جستجو
            if result:
                print('Contact found:', result)
            else:
                print('Contact not found!')

        # خروج از برنامه
        case 0:
            break

        # مدیریت انتخاب‌های نامعتبر کاربر
        case _:
            print('Error: Invalid choice! ')
    print('----------------------------------')

