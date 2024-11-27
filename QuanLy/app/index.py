import math
from itertools import product

from flask import render_template, request, redirect
import dao
from app import app, login
from flask_login import login_user, logout_user


@app.route("/")
def index():
    cates = dao.load_categories()

    cate_id = request.args.get('category_id')
    kw = request.args.get('kw')
    from_price=request.args.get("from_price",type=int)
    to_price=request.args.get("to_price",type=int)
    page = request.args.get('page', 1,type=int)

    if from_price:
        from_price = float(from_price)
    if to_price:
        to_price = float(to_price)

    prods = dao.load_products(cate_id=cate_id, kw=kw, from_price=from_price, to_price=to_price,page=int(page))

    total = dao.count_products()
    page_size = app.config['PAGE_SIZE']
    return render_template('index.html', categories=cates, products=prods, pages=math.ceil(total / page_size),
                           from_price=from_price, to_price=to_price)


@app.route("/login", methods=['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        u = dao.auth_user(username=username, password=password)
        if u:
            login_user(u)
            return redirect('/')

    return render_template('login.html')


@app.route("/logout", methods=['get', 'post'])
def logout_process():
    logout_user()
    return redirect("/login")


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True, port=9999)