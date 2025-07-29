from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add():
    amount = request.form.get('amount')
    category = request.form.get('category')
    expenses.append({'amount': amount, 'category': category})
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
