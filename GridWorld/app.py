from flask import Flask, render_template, request 
 
app = Flask(__name__) 
 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
    if request.method == 'POST': 
        n = int(request.form.get('n'))       
        gamma = float(request.form.get('gamma')) 
        alpha = float(request.form.get('alpha')) 
        if n < 3 or n > 20: 
            return render_template('index.html', error='Invalid value for n. n must be between 3 and 20.') 
        else: 
            return render_template('square.html', n=n, gamma=gamma, alpha=alpha) 
    else: 
        return render_template('index.html') 
 
if __name__ == '__main__': 
    app.run(debug=True) 
