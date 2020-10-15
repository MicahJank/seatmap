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
    if seat['column_letter'] == 'A' or seat['column_letter'] == 'B':
        left.append(seat)
    elif seat['column_letter'] == 'C' or seat['column_letter'] == 'D' or seat['column_letter'] == 'E':
        middle.append(seat)
    else:
        right.append(seat)


print(left)
# print(middle)
# print(right)
@app.route('/', methods=["GET", "POST"])
def index():
    # total will be updated based on the seat the user selects
    total = 0 
    if request.method == "GET":
        print("get")
    elif request.method == "POST":
        if request.form['seat']:
            total = request.form['seat']
    
    return render_template('index.html', left=left, right=right, middle=middle, value=total)
    

# @app.route('/<name>')
# def index(name):
    


if __name__ == '__main__':
    app.run()