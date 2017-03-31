from flask import Flask
app = Flask(__name__)


import csv

f= open('data/strikes_by_president.csv')
csv_f = csv.reader(f)

for row in csv_f:
    print row

print
print
print

g= open('data/strike_data.csv')
csv_g = csv.reader(g)

for row in csv_g:
        print row


    
@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
