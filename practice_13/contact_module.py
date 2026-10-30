# ایجاد لیست خالی برای ذخیره مخاطبین
contact_list = []


# نمایش منوی اصلی و دریافت انتخاب کاربر
def show_menu():
    print('1)Add contact')
    print('2)Contact list')
    print('3)Search by phone number')
    print('0)Exit')
    option = int(input('Enter your choice:'))
    return option


# دریافت اطلاعات مخاطب از کاربر و برگرداندن آن به صورت دیکشنری
def get_contact_information():
    name = input('Enter a name:')
    family = input('Enter a family:')
    phone = input('Enter a phone:')
    title = input('Enter a title:')
    return {'name': name, 'family': family, 'phone': phone, 'title': title}


# نمایش تمام مخاطبین ذخیره شده در لیست
def print_contact_list(contact_list):
    print('Contact list:')
    if not contact_list:
        print('Contact list is empty!')
        return
    for contact in contact_list:
        print(
            f"name:{contact['name']:10} family:{contact['family']:10} phone:{contact['phone']:<10} title:{contact['title']:10}")


# جستجوی مخاطب بر اساس شماره تلفن
# در صورت پیدا شدن مخاطب٫ اطلاعات آن را برمی گرداند
def find_contact_by_phone(contact_list, phone):
    for contact in contact_list:
        if contact['phone'] == phone:
            return contact
    return None