from flask import Flask,render_template,request
from model import generate_response
app = Flask(__name__)

# user_text = []
response_text = []

@app.route('/',methods=['GET'])
def chatbot():
    if(request.method=='GET'):
        return render_template('index.html',response_text=response_text)
    
@app.route('/response',methods=['POST'])
def response():
    #write the logic to get response and return render template to index.html
    if(request.method=='POST'):
        user_input = request.form['user_text']

        response_text.append((user_input,generate_response(user_input)))
        print(response_text)
        # return redirect('/')
        return render_template('index.html',response_text=response_text)
    

if __name__ == '__main__':
    app.debug = True
    app.run() 