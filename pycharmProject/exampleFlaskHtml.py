from flask import Flask, render_template
import os

html_file = "exampleFlaskHtml.html"
output_html_path = "C://python/pycharmProject/" + html_file

app = Flask(__name__)


@app.route("/")
def index():
    fp = open(output_html_path, "w")
    fp.write("<html>\n")
    fp.write("<head>\n")
    fp.write("</head>\n")
    fp.write("<body>\n")
    fp.write("<table border=\"1\">\n")
    fp.write("<tr><td>book</td></tr>\n")
    fp.write("<tr><td>pencil</td><td>eraser</td></tr>\n")
    fp.write("</table>\n")
    fp.write("</body>\n")
    fp.write("</html>")
    fp.close()

    return render_template('exampleFlaskHtml.html')

@app.route("/page2")
def page2():
    return render_template("htmlTemplate.html")

app.run(debug=True, host='10.192.183.140', port=5001)
