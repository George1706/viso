from flask import render_template
from app import app


@app.route('/')
def inicio():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True, port=5000)
