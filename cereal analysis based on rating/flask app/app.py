from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
model = pickle.load(open('cerealanalysis.pkl','rb'))

@app.route('/')
def helloworld():
    return render_template("base.html")

@app.route('/assesment')
def prediction():
    return render_template("index.html")

@app.route('/predict', methods = ['POST'])
def admin():
    a= request.form["mfr"]
    if (a == 'a'):
        a1,a2,a3,a4,a5,a6,a7=1,0,0,0,0,0,0
    if (a == 'g'):
        a1,a2,a3,a4,a5,a6,a7=0,1,0,0,0,0,0
    if (a == 'k'):
        a1,a2,a3,a4,a5,a6,a7=0,0,1,0,0,0,0
    if (a == 'n'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,1,0,0,0    
    if (a == 'p'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,1,0,0    
    if (a == 'q'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,1,0    
    if (a == 'r'):
        a1,a2,a3,a4,a5,a6,a7=0,0,0,0,0,0,1    
        
    b= request.form["type"]
    if (b == 'c'):
        b=0
    if (b == 'h'):
        b=1
    c= request.form["Calories"]
    d= request.form["Protien"]
    e= request.form["Fat"]
    f= request.form["Sodium"]
    g= request.form["Fiber"]
    h= request.form["Carbo"]
    i= request.form["Sugars"]
    j= request.form["Potass"]
    k= request.form["Vitamins"]
    l= request.form["Shelf"]
    m= request.form["Weight"]
    n= request.form["Cups"]

    t=[[int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(b),int(c),int(d),int(e),int(f),float(g),float(h),int(i),int(j),int(k),float(l),float(m),float(n)]]        
    y = model.predict(t)
    return render_template("prediction.html", z = y[0][0])



if __name__ == '__main__':
    app.run(debug = False)

