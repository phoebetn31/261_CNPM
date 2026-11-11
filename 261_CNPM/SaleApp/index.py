from flask import render_template, request
from werkzeug.utils import redirect

import dao
from SaleApp import app



@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    return render_template("index.html", prods=dao.load_products(q=q, cate_id=cate_id))

@app.route("/product/<int:id>")
def details(id):
    return render_template("prod_detail.html", prod=dao.get_product_by_id(id))

@app.route("/login", methods=["get","post"])
def login_my_user():
    err_msg = None
    if request.method.__eq__("POST"):
        user = request.form.get("username")
        password = request.form.get("password")

        if user == "user" and password == "123":
            return redirect("/")
        else:
            err_msg = "Tài khoản hoặc mật khẩu không chính xác!"
    return render_template("login.html", err_msg=err_msg)

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }


if __name__=="__main__":
    app.run(debug=True)