from flask import Flask, render_template  # Import Flask to allow us to create our app
import math
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return f"Add /play to end of address!"

@app.route('/play')
def play(num = 3):
    return render_template("index.html", times = int(num), colr = 'aqua')

@app.route('/play/<num>')
def playNum(num):
    rowz = math.trunc(int(num) / 4) + 1
    return render_template("index.html", times = int(num), colr = 'aqua', rows = rowz)

@app.route('/play/<num>/<clr>')
def playNumColor(num, clr):
    rowz = math.trunc(int(num) / 4) + 1
    return render_template("index.html", times = int(num), colr = clr, rows = rowz)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.