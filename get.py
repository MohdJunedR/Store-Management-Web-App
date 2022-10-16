 
import data as d
menu='''
    1.Add Product
    2.Update Product
    3.Delete product
    4.Show Product list
    5.Show single product
    
    Select your choice
'''

choice=int(input(menu))
if choice==1:
    name=input("Enter Product Name:")
    price=float(input("Enter product Price:"))
    row=d.insert(name, price)
    print(f"{row} row inserted")

elif choice==2:
    productid=int(input("Enter book id to update:"))
    product=d.get_single_product(productid)
    if bool is not None:
        print("old Product details")
        print(product)
        name=input("Enter Product Name:")
        price=float(input("Enter Product Price:"))
        row=d.update(productid, name, price)
        print(f"{row} rows update succesfully")
    else:
        print("Entered product id is not found")
 
elif choice==3:

    productid=int(input('Enter book id to delete book'))
    product=d.get_single_product(productid)
    if product:
        print(product)
        yes_no=input("Do you want to delete Product:")
        if yes_no in['y','Y',"Yes","yes"]:
            d.delete(productid)
            print("Productis Deleted")
    else:
        print("Enter Product Id is Invalid")

elif choice==4:
    productlist=d.all()
    if productlist:
        print("-"*5,"Product List","-"*5)
        for product in productlist:
            print(*product)
            print("-"*30)
        else:
            print("-"*30)
    else:
        print("Product not found")
    
elif choice==5:
    productid=int(input("Enter Product id:"))
    product=d.get_single_product(productid)
    print(product)



    
    
