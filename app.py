from flask import Flask,render_template
from flask import url_for,redirect
from flask import request as req

import data as d
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/productlist")
def productlist():
    plist=d.all()
    return render_template("productlist.html",plist=plist)


@app.route("/productdelete/<int:productid>")
def deleteproduct(productid):
    d.delete(productid)
    return redirect(url_for("productlist"))



@app.route("/productadd",methods=['POST','GET'])
def productadd():
    if req.method=='GET':
        return render_template("addproduct.html")
    elif req.method=='POST':
        name=req.form["productname"]
        price=req.form.get("productprice")

        d.insert(product_name=name, product_price=price)
        return redirect(url_for("productlist"))

@app.route("/productupdate/<int:productid>" ,methods=['POST','GET'])
def updateproduct(productid):
    if req.method=='GET':
        product=d.get_single_product(productid)
        return render_template("updateproduct.html",product=product)
    
    elif req.method=='POST':
            
        name=req.form.get("productname")
        price=req.form.get("productprice")
        d.update(product_name=name,product_price=price,product_id=productid)
        return redirect(url_for("productlist"))





if __name__=="__main__":
    app.run(debug=True)


