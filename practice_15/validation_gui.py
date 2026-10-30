# وارد کردن کتابخانه‌های مورد نیاز برای ایجاد رابطه گرافیکی
from tkinter import *
from tkinter import messagebox
# وارد کردن توابع اعتبارسنجی از ماژول
from validation_module import *

# ایجاد لیست برای نگهداری اطلاعات اعتبارسنجی شده
finish_list = []


# بررسی اطلاعات وارد شده با کلیک روی دکمه اعتبارسنجی
def valid_click():
    try:
        # بررسی اعتبار اطلاعات و دریافت نتایج
        validator_click = {
            "National_id": check_national_id(national.get()),
            "Phone number": check_phone_number(phone.get()),
            "Card number": check_card_number(card.get()),
            "Car plate": check_car_plate(plate.get()),
            "Bill": check_bill_id(bill.get(), payment.get())
        }

        # افزودن اطلاعات معتبر به لیست
        finish_list.append(validator_click)
        # نمایش پیام موفقیت آمیز بودن عملیات
        messagebox.showinfo("Saved", "Information Saved")

        # پاک کردن فیلدهای ورودی پس از ثبت اطلاعات
        national.set('')
        phone.set('')
        card.set('')
        plate.set('')
        bill.set('')
        payment.set('')

    # دریافت و نمایش خطاهای احتمالی
    except Exception as e:
        messagebox.showerror("Save Error", f"Error {e}")


# ایجاد پنجره اصلی برنامه
window = Tk()
# تنظیم ابعاد و عنوان پنجره
window.geometry('500x400')
window.title('Information Validation System')

# ایجاد فیلد ورود کد ملی
Label(window, text='National Id', bg=window.cget('bg')).place(x=5, y=10)
national = StringVar()
Entry(window, textvariable=national).place(x=100, y=10)

# ایجاد فیلد ورود شماره موبایل
Label(window, text='Phone Number', bg=window.cget('bg')).place(x=5, y=40)
phone = StringVar()
Entry(window, textvariable=phone).place(x=100, y=40)

# ایجاد فیلد ورود شماره کارت بانکی
Label(window, text='Card Number', bg=window.cget('bg')).place(x=5, y=70)
card = StringVar()
Entry(window, textvariable=card).place(x=100, y=70)

# ایجاد فیلد ورود پلاک خودرو
Label(window, text='Car Plate', bg=window.cget('bg')).place(x=5, y=100)
plate = StringVar()
Entry(window, textvariable=plate).place(x=100, y=100)

# ایجاد فیلد ورود شناسه قبض
Label(window, text='Bill Id', bg=window.cget('bg')).place(x=5, y=130)
bill = StringVar()
Entry(window, textvariable=bill).place(x=100, y=130)

# ایجاد فیلد ورود شناسه پرداخت
Label(window, text='Payment Code', bg=window.cget('bg')).place(x=5, y=160)
payment = StringVar()
Entry(window, textvariable=payment).place(x=100, y=160)

# ایجاد دکمه اعتبارسنجی و اتصال آن به تابع
Button(window, text='Validation', command=valid_click).place(x=400, y=300)

# اجرای حلقه‌ اصلی برنامه
window.mainloop()