from flask import Flask

app = Flask (__name__)

def calculation(a,b):
    c = a + b
    return c

def new_function(a,b,c): #Новая функция
    x= a*b/c
    return x

@app.route("/")
def index():

    return "This is payment page! Please pay $s USD."%(calculation(10, 20))

if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=8080, debug=True)