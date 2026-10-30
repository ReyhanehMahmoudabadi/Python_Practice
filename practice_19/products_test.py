from products import *

# tested
# ایجاد شیء اول از کلاس Iphone
product_1 = Iphone()

# مقداردهی ویژگی‌های محصول اول
product_1.name = 'pro17'
product_1.price = 120000000
product_1.voltage = 4
product_1.display_size = 7
product_1.serial = 'UL7844654'

# نمایش مشخصات محصول اول
print(product_1)
# -----------------------------

# tested
# ایجاد شیء دوم از کلاس Furniture
product_2 = Furniture()

# مقداردهی ویژگی‌های محصول دوم
product_2.name = 'Chester sofa'
product_2.price = 180000000
product_2.capacity = 5
product_2.weight = 90
product_2.color = 'brown'

# نمایش مشخصات محصول دوم
print(product_2)