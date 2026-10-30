# برنامه ایی که تا وقتی کاربر کلمه exite وارد نکرده ، اسم بگیرد و درآخر یکی یکی آنها را به ترتیب حروف الفبا چاپ کند
name_list = []

# دریافت اسم تا زمانی که کاربر کلمه exit وارد کند
while True:
    name = input('Enter a name:')
    # بررسی اینکه اسم وارد شده کلمه exit است یا خیر
    if name.lower() == 'exit':
        break
    #  افزودن اسامی به لیست
    name_list.append(name)
print(name_list)

# خط جدا کننده دو بخش خروجی
print('----------------------')

# مرتب کردن اسامی لیست به ترتیب حروف الفبا
name_list.sort()

print('Names in alphabetical order:')
# چاپ اسامی به ترتیب حروف الفبا به صورت یکی یکی
for name in name_list:
    print(name)