from flask import Flask, render_template, url_for, redirect, request
import requests


app = Flask(__name__)

response = requests.get('https://my.api.mockaroo.com/seats?key=0523bb20')
seats = response.json()
left = []
middle = [] 
right = [] 

# data needs to be split between left right and middle to display it properly
for seat in seats:
    if seat['row_number'] == 'A' or seat['row_number'] == 'B':
        left.append(seat)
    elif seat['row_number'] == 'C' or seat['row_number'] == 'D' or seat['row_number'] == 'E':
        middle.append(seat)
    else:
        right.append(seat)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        print(request.form)
    
    return render_template('index.html', left=left, right=right, middle=middle, value="Hello")
    

# @app.route('/<name>')
# def index(name):
    


if __name__ == '__main__':
    app.run()