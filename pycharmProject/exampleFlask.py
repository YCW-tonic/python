from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    # array = [0,1,2,3]
    # print(array[4])

    return "This is Index."

@app.route("/page2")
def page2():
    return "This is Page2."

@app.route("/page3")
def page3():
    return "<h1>This is Page3.</h1><p>These are contents.</p>"
app.run(debug=True,host='10.192.183.140',port=5000)