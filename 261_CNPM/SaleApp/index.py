from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import dao

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    print(q)
    cates = dao.load_categories()
    prods = dao.load_products(q=q, cate_id=cate_id)
    return render_template("index.html", cates=cates, prods=prods)

@app.route("/product/<int:id>")
def details(id):
    return render_template("prod_detail.html", prod=dao.get_product_by_id(id))

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }


if __name__ == "__main__":
    app.run(debug=True)