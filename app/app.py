from flask import Flask, render_template, url_for, redirect
import requests


app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://my.api.mockaroo.com/seats?key=0523bb20')

    seats = response.json()
    # i seperate them into two halfs to be able to seperate them in the layout in the html and css
    top_half = seats[:len(seats)//2]
    bot_half = seats[len(seats)//2:]
    return render_template('index.html', top_half=top_half, bot_half=bot_half)
    

# @app.route('/<name>')
# def index(name):
    


if __name__ == '__main__':
    app.run()