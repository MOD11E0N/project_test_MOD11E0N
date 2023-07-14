from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Maryem_OUAMMOU is the smartest cutest girl ever!'
if __name__ == '__main__':
    app.run(debug=True)
