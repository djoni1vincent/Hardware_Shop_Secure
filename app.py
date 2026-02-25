from flask import Flask, redirect, render_template, session, url_for

products = [
    {'id': 1, 'name': 'Gaming mus', 'price': 499},
    {'id': 2, 'name': 'Mekanisk tastatur', 'price': 1299},
    {'id': 3, 'name': 'Skjerm 27"', 'price': 2500}
]

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():

    last_viewed = session.get('last_viewed', [])

    return render_template('index.html', title='Home', products=products, last_viewed=last_viewed)

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




if __name__ == '__main__':
    app.run(debug=True)
