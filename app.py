from flask import Flask, redirect, render_template, session, url_for

products = [
    {"id": 1, "name": "Gaming mus", "price": 499},
    {"id": 2, "name": "Mekanisk tastatur", "price": 1299},
    {"id": 3, "name": "Skjerm 27\"", "price": 2500},
    {"id": 4, "name": "Trådløst Headset", "price": 899},
    {"id": 5, "name": "RGB Musematte", "price": 299},
    {"id": 6, "name": "Grafikkort RTX 4060", "price": 4500},
    {"id": 7, "name": "Gaming Stol", "price": 1999},
    {"id": 8, "name": "Webkamera 4K", "price": 1150},
    {"id": 9, "name": "Mikrofon (USB)", "price": 750},
    {"id": 10, "name": "Prosessor i7-14700K", "price": 5200},
    {"id": 11, "name": "SSD 2TB NVMe", "price": 1400},
    {"id": 12, "name": "RAM 32GB DDR5", "price": 1650}
]

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a-very-secret-and-long-string'

@app.route('/')
def index():
    session['key'] = 'value'
    last_viewed = session.get('last_viewed', [])

    return render_template('index.html', title='Home', products=products, last_viewed=last_viewed)


@app.route('/privacy')
def privacy():
    return render_template('privacy.html', title='Privacy Policy')

@app.route('/add/<int:prod_id>')
def add_to_cart(prod_id):
    if 'cart' not in session:
        session['cart'] = []

    cart = session['cart']
    cart.append(prod_id)
    session['cart'] = cart

    product_name = next((p['name'] for p in products if p['id'] == prod_id), "Ukjent vare")

    last_viewed = session.get('last_viewed', [])
    if product_name not in last_viewed:
        last_viewed.insert(0, product_name)
        session['last_viewed'] = last_viewed[:5]

    return redirect(url_for('index'))


@app.route('/cart')
def view_cart():
    cart_ids = session.get('cart', [])
    cart_items = []
    total_price = 0

    for item_id in cart_ids:
        for product in products:
            if product['id'] == item_id:
                cart_items.append(product)
                total_price += product['price']
                break

    return render_template('cart.html', title='Cart', cart_items=cart_items, total=total_price, clear_cart=clear_cart)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('view_cart'))

if __name__ == '__main__':
    app.run(debug=True)
