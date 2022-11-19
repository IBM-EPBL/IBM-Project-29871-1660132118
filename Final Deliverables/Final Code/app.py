from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/products')
def products():
    return render_template('products.html')
if __name__ == "__main___":
    app.run(host="0.0.0.0", port=5000)