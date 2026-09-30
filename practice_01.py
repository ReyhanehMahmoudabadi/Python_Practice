#قد برحسب سانتی متر
height_cm=160

#وزن بر حسب کیلو گرم
weight=60

#تبدیل قد از سانتی متر به متر
height_m=height_cm/100

#محاسبه BMI
bmi=weight/(height_m**2)

#چاپ BMI
print('BMI :',bmi)