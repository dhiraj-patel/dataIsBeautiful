from flask import Flask, render_template, url_for
app = Flask(__name__)

def presidents():
	import csv
	f= open('data/strikes_by_president.csv')
	csv_f = csv.reader(f)
	data = ""
	k = 0
	x = open('data/strikes_by_president.tsv','a')
   	#with open ('data/strikes_by_president.txt', 'a') as proc_seqf:
   	for row in csv_f:
   		y = ""
		i = 0
		if k !=0:
			for elem in row:
				if i == 0:
					y = y + elem + "/t "
			
				if i == 1:
					y = y + elem
				i+=1
                
		k+=1
        x.writerow(y)
	x.close()
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
	#return url_for('static', filename='strikes.html')
    return render_template('home.html')

if __name__ == '__main__':
    app.run()

presidents()
