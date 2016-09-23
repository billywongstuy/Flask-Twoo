from flask import Flask, render_template
app = Flask(__name__)
import csv
import random

def chooseJob():
    sheet = csv.reader(open("occupations.csv"))
    jobs = {}


    for row in sheet:
        if row[0] != "Total" and row[1] != "Percentage":
            job = row[0]
            percent = float(row[1])
            jobs[job] = percent


    tracker = float(random.randrange(998))/10


    for key in jobs:
        if tracker != 20000:
            if jobs[key] >= tracker:
                tracker = 20000
                return key          
            else:
                tracker -= jobs[key]


def beginning(title):
    return '''
    <!DOCTYPE html>
    <html>
    <head>''' + title + '''

    <link href='http://fonts.googleapis.com/css?family=Ubuntu:400,500,700' rel='stylesheet' type='text/css'>
    <link type="text/css" rel="stylesheet" href="static/index-stylesheet.css">

    <style>
    body {font-family: Ubuntu}
    </style>

    </head>
    <body>    
    '''

def end():
    return '''
    </body>
    </html>
    '''

def makeTable():
    store = "<table border=\"1px\">"
    sheet = csv.reader(open("occupations.csv"))
    for row in sheet:
        store += "<tr>"
        store += "<td>" + row[0] + "</td><td>" + row[1] + "</td>" 
        store += "</tr>"
    store += "</table></br>"
    return store


@app.route("/")
def helloworld():
    return render_template("index.html")

@app.route("/occupations")
def occupy_wallstreet():
    text = beginning("Occupations") + "<div id=\"header\" style=\"font-family:'Ubuntu';\">" + makeTable() + "</br>" + chooseJob()+ "</div>" + end() 
    return text

@app.route("/fun")
def test_temp():
    stuff = '''
    This is an almost blank page. </br> 
    Oh, and Jinja2, if you put "|safe" after a variable, html tags work!
    '''
    return render_template("template.html",Title="Fun",body=stuff)


if __name__ == "__main__":
    app.debug = True
    app.run()

