product_id= int(input('Enter Product Id:-'))
product_name= str(input('Enter product name :-'))
product_price= int(input('Enter product price :-'))
product_Qty= int(input('Enter Product Quentity :-'))


total_price=product_price*product_Qty
discounted_price=total_price-(0.07*product_price)
Gst_price=discounted_price+(5.81*product_Qty)
saved_money=total_price-discounted_price
print('------------------------------------------')
print('****************[T sweet]*****************')
print('product:-',product_name)
print('Price:-',product_price)
print('Qty:-',product_Qty)
print('Total Price:-',discounted_price)
print('With GST & SGST:-',round(Gst_price))
print('Saved Money:-',saved_money)
print('------------------------------------------')
