from flask import Flask, render_template
app = Flask(__name__)









def presidents():
	import csv
	f= open('data/strikes_by_president.csv')
	csv_f = csv.reader(f)
	data = ""
	k = 0
	for row in csv_f:
		i = 0
		if k !=0:
			for elem in row:
        
				if i == 0:
					data = data + elem + ", "
			
				if i == 1:
					data = data + elem + "/n "
				i+=1
		k+=1
	print data
	return data


'''
g= open('data/strike_data.csv')
csv_g = csv.reader(g)

for row in csv_g:
        print row
'''

    
@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

presidents()
