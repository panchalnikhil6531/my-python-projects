product_code = int(input("Enter the product code (1 for battery, 2 for key, 3 for charging): "))
order_amount = float(input("Enter the order amount (in Rs.): "))

if product_code==1:
    if order_amount>50:
        print("Discou = ",order_amount*0.10)
        print("Bill = ",order_amount-order_amount*0.10)
    elif order_amount<50:
        print("Discou = ", order_amount * 0.05)
        print("Bill = ", order_amount - order_amount * 0.05)


elif product_code==2:
     if order_amount>40:
         print("discount =",order_amount*0.15)
         print("bill=", order_amount-order_amount*0.15)
     elif order_amount<40:
         print("Discou = ", order_amount * 0.10)
         print("Bill = ", order_amount - order_amount * 0.10)

elif product_code==3:
    if order_amount>60:
        print("discount =",order_amount*0.25)
        print("bill=", order_amount-order_amount*0.25)
    elif order_amount<60:
        print("Discou = ", order_amount * 0.10)
        print("Bill = ", order_amount - order_amount * 0.10)

