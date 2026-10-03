# برنامه دریافت کالا تا زمانی که مجموع قیمت به یک میلیون برسد
product_list = []
total_price = 0

# حلقه دریافت اطلاعات کالا
while True:
    name = input('Enter the product name:')
    quantity = int(input('Enter the quantity:'))
    price = int(input('Enter the price:'))

    # ذخیره اطلاعات کالا به صورت دیکشنری
    product = {'name': name,
               'quantity': quantity,
               'price': price
               }

    # محاسبه مجوع قیمت کالاها
    total_price += price * quantity
    print('Total price before adding:', total_price)

    # اگر مبلغ کل یک میلیون یا کمتر از آن بود، کالای جدید دریافت شود
    if total_price <= 1000000:
        product_list.append(product)
        print('Total price after adding to the list', total_price)
        print('Product saved!!!')

    # درغیر این صورت (کالا بیشتر از 1میلیون شد) از حلقه خارج شود
    else:
        print('Maximum amount reached!!!')
        break

    # اگر کالا یک میلیون شده باشد دیگر به حلقه ادامه نمیدهد و خارج میشود
    if total_price == 1000000:
        break

# چاپ لیست کالاها به صورت مرتب
print('Print the final list :')
for product in product_list:
    print(f"Name={product['name']:10} |Quantity= {product['quantity']} |Price= {product['price']}")