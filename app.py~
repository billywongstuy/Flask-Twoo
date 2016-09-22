from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "No mine <a href=\"first_temp\">Here</a>"

@app.route("/secret")
def secsec():
    return '''
    <!DOCTYPE html>
    <html>
    <body>
    Hello! Can you read this?
    </body>
    </html>
    '''

@app.route("/notsecret")
def something():
    return "you cannot read this"


coll = [1,2,3,4,5]

@app.route("/first_temp")
def test_temp():
    return render_template("main.html",foo="SILENCIO",thing=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()

