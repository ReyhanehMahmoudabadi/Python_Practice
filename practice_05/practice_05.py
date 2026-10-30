#میانگین پنج نمره دریافتی
scores={}

#وارد کردن 5 درس و نمرات مربوطه
for i in range(5):
    subject=input('Enter the subject name:')
    #دریافت و بررسی نمره
    while True:
        try:
            score=float(input('Enter the number:'))
            #بررسی معتبر بودن نمره
            if 0<=score<=20:
                scores[subject]=score
                break
            else:
                print('Invalid score!!!')

        #مدیریت ورود مقدار غیر عددی
        except ValueError:
            print('please enter a number!!!')

#چاپ دیکشنری درس ها و نمرات
print('Scores:',scores)

#محاسبه میانگین 5 نمره وارد شده
avg=sum(scores.values())/len(scores)
print('Average scores:',avg)