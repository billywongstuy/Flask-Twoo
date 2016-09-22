from flask import Flask, render_template
app = Flask(__name__)

import csv
import random

sheet = csv.reader(open("occupations.csv"))
sheet.next()
jobs = {}


##GET OCCUPATIONS.CSV

for row in sheet:
    if row[0] != "Total":
        job = row[0]
        percent = float(row[1])
        jobs[job] = percent

#print jobs 

tracker = float(random.randrange(998))/10

print "Random: " + str(rand)


#This is kind of unefficient because the loop doesn't
#stop until the last value no matter what
for key in jobs:
    if tracker != 20000:
        if jobs[key] >= tracker:
            print key 
            tracker = 20000
        else:
            tracker -= jobs[key]


def beginning(String title):
    return '''
    <!DOCTYPE html>
    <html>
    <head>''' + title + '''</head>
    <body>
    
    '''

def end():
    return '''
    </body>
    </html>
    '''

@app.route("/")
def helloworld():
    return render_template("index.html")

@app.route("/occupations")
def occupy_wallstreet():
    return 

@app.route("/notsecret")
def something():
    return "you cannot read this"


coll = [1,2,3,4,5]

@app.route("/first_temp")
def test_temp():
    return "none"
    #return render_template("main.html",foo="SILENCIO",thing=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()

