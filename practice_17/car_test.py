from car import Car

# tested
# ایجاد شئ اول از کلاس Car
car_1 = Car()

# مقدار دهی ویژگی های خودروی اول
car_1.name = 'Benz'
car_1.color = 'Red'
car_1.plate = '12345R67'

# ذخیره اطلاعات و نمایش مشخصات خودروی اول
print(car_1.save())
print(car_1)

# --------------------------

# tested
# ایجاد شئ دوم از کلاس Car
car_2 = Car()

# مقدار دهی ویژگی های خودروی دوم
car_2.name = 'BMW'
car_2.color = 'White'
car_2.plate = '1111Z22'

# ذخیره اطلاعات و نمایش مشخصات خودروی دوم
print(car_2.save())
print(car_2)
