from Chain import Chain
from flask import Flask, render_template, request
app = Flask(__name__)

my_chain = Chain()

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", blocks = my_chain.block_chain)

#to add a transaction "/add?tx=some-transaction"
@app.route("/add")
def add():
    query = request.args.get('tx')
    my_chain.add_data(query)
    return render_template("add.html",query = query, message = "query added")

@app.route("/mine")
def mine():
    message = my_chain.create_block()
    return render_template("mine.html", message = message)

if __name__ == '__main__':
    app.run(debug=True)






