import pymysql as pm

con =pm.connect(host="localhost",user="root",password="",database="store")


def insert(product_name,product_price):
    cursor=con.cursor()
    sqlquery="insert into storetb (product_name,product_price)values(%s,%s)"
    i=cursor.execute(sqlquery,(product_name,product_price))
    con.commit()
    return i

def update(product_id,product_name,product_price):
    cursor=con.cursor()
    sqlquery="update storetb set product_name=%s,product_price=%s where product_id=%s"
    i=cursor.execute(sqlquery,(product_name,product_price,product_id))
    con.commit() 
    return i


def delete(product_id):
    cursor=con.cursor()
    sqlquery="delete from storetb where product_id=%s"
    i=cursor.execute(sqlquery,(product_id))
    con.commit() 
    return i

def all():
    cursor=con.cursor()
    sqlquery="select *from storetb"
    cursor.execute(sqlquery)
    rows= cursor.fetchall()
    return rows

def get_single_product(product_id):
    cursor=con.cursor()
    sqlquery="select *from storetb where product_id=%s"
    cursor.execute(sqlquery,(product_id))
    row=cursor.fetchone()
    return row






