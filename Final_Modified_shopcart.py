#28/10/21
#geethanjali
#modified shopping cart


def start():
    print("Welcome to *soft-touch* shopping")

    while True:
        print("\n please login to enter!")
        user_type=['1.admin','2.user', '3.Exit']
        print(user_type[0])
        print(user_type[1])
        print(user_type[2])
        user_type=input("Enter the user type : ")
        if user_type=="1":
            admin()
        if user_type=="2":
            user()
        if user_type=="3":
            print("Thanks for coming,meet you later.bye.....")
            break
        
def admin():
       # x=admin_list[x]
        
        admin_name=input("Enter the admin Name : ")
        password=input("Enter the password : ")
        A=admin_list.index(admin_name)
        B=passwords.index(password)

        if A==B:
            admin_choice()

        else:
            print("\ninvalid user name or password, please try again.\n")
            start()
    
def admin_choice():
    print("you choice:")
    print("\n 1.Add item   2.Delete item 3.update item  4.add admin  5.Exit")
    choice=input("Enter the choice : ")
    if choice=="1":
        add()
    if choice=="2":
        delete()
    if choice =="3":
        item_update()
    if choice == "4":
        add_admin()
        
    if choice == "5":
        start()
        
def add():
        
        add_item=input("enter the adding item : ")
        if add_item not in items or add_item in items :
            items.append(add_item)
            print(items)
                
        add_quantity=input("enter the adding quantity of item : ")
        if add_quantity not in quantities or add_quantity in quantities:
            quantities.append(add_quantity)
            print(quantities)
            

        add_price=input("enter the adding price of  item : ")
        if add_price not in prices or add_price in prices:
            prices.append(add_price)
            print(prices)
            
        admin_choice()

def add_admin():
    add_admin_name=input("Enter the admin name you want to add : ")
    ad_password=input("Enter the password : ")
    admin_list.append(add_admin_name)
    passwords.append(ad_password)
    print(admin_list)
    print(passwords)
    admin_choice()
    

def delete():
       
        del_item=input("enter the item to delete : ")
        t=items.index(del_item)
        del items[t]
        del quantities[t]
        del prices[t]
        print(items)
        print(quantities )
        print(prices)
        admin_choice()

def item_update():
    print("\n 1.update quantity  2.update price  3.update quantity and price  4.Exit")
    choice=input("Enter the choice : ")
    if choice=="1":
        item_update=input("Enter the item name : ")
        quantity_update=input("Enter the quantity : ")
        p=items.index(item_update)
        quantities[p]=quantity_update
        print(items)
        print(quantities)
        
    if choice=="2":
        item_update=input("Enter the item name : ")
        price_update=input("Enter the price : ")
        q=items.index(item_update)
        prices[q]=price_update
        print(items)
        print(prices)

    if choice=="3":
        item_update=input("Enter the item name : ")
        quantity_update=input("Enter the quantity : ")
        price_update=input("Enter the price : ")
        p=items.index(item_update)
        q=items.index(item_update)
        quantities[p]=quantity_update
        prices[q]=price_update
        print(items)
        print(quantities)
        print(prices)

  
    if choice == "4":
        admin_choice()
  
               
def delete_shop_item():
    print("your shopping list is :",shopcart_item)
    print("Your shopping quantity :",shop_item_qty)
    print("Your shopping price :",shop_item_prc)

    del_shop=input("Enter the delete item : ")
    if del_shop in shopcart_item:
        #a=items.index(del_shop)
        x=shopcart_item.index(del_shop)
        y=shop_item_qty[x]
        z=shop_item_prc[x]
        del shopcart_item[x]
        del shop_item_qty[x]
        del shop_item_prc[x]
        h=items.index(del_shop)
        quantities[h]=int(quantities[h]) + int(y)
        total_payment[0]= int(total_payment[0])- int(z)
        print("After deleting the item ")
        print("Your Final payment is", total_payment[0])
        print(items)
        print(quantities)
        user()

    

def user():
    print("""
                  a.puchase the items
                  b.delete item from list
                  c.Exit
                  """)
    choice=input("Enter the choice : ")


    if choice=="a":
        print("\n")
        print( "Available Items ")
        print(items)
        #print(quantities)
        #print(prices)
            
        print("\n")
        shopcart_item=[]
        
        total_amount=0
        buy_items()
    if choice == "b":
        delete_shop_item()
    if choice =="c":
        start()

def buy_items():
    total=0
    print(items)
    user_item=input("Enter the item : ")
    if user_item in items:
        a=items.index(user_item)
        shopcart_item.append(user_item)
        x=shopcart_item.index(user_item)
        
        # item_input=items[item]
        quantity=input("Enter the quantity : ")
        shop_item_qty.append(quantity)
        y=quantities[a]
        
        print(y)
        if int(quantity) <= int(y):
            price=int(quantity)*int(prices[a])
            print("Your shopping list : ", str(shopcart_item))
            print("You want to pay for purchase this item : ", price)
            shop_item_prc.append(price)
            quantities[a]=int(quantities[a]) - int(quantity)
            print("your shopping list : ",shopcart_item)
            print("Your shopping quantity :",shop_item_qty)
            print("Your shopping price :",shop_item_prc)


            print("Remaning available quantity is : ",quantities[a])
            total_payment[0]= int(total_payment[0])+int(price)
            print("Your Final payment is", total_payment[0])
            user()
        else:
            print("stock input too much .")
            buy_items()
        
       

    if user_item not in items:
        print("Please enter the available items only")

       
shopcart_item=[]
shop_item_qty=[]
shop_item_prc=[]
items=['bangle','earing','chain','ring']
quantities=['200','160','140','300']
prices=['1000','500','1500','250']
admin_list=['geetha','anjali','pavi']
passwords=['g123','a123','p123']
total_payment=['0']

        
start()
                
           






