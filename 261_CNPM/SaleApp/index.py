from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    print(q)
    cates = dao.load_categories()
    prods = dao.load_products(q=q, cate_id=cate_id)
    return render_template("index.html", cates=cates, prods=prods)

@app.route("/product/<int:id>")
def detail(id):
    return render_template("prod_detail.html", id=id, prods=prods)


if __name__ == "__main__":
    app.run(debug=True)