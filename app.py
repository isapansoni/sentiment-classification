from flask import Flask,request,jsonify , render_template
from flask_cors import CORS
import json
import os
from cls import prediction_return

app = Flask(__name__)
CORS(app) 



@app.route('/',methods =['GET','POST'])
def index():
    
    return render_template('index.html')

        
@app.route('/get_sentiment/',methods =['GET','POST'])
def recommend_movie_list():
    request.get_data()
    try:
        data = request.data
    except:
        try:
            data = request.json
        except:
            try:
                data = request.args
            except:
                data = request.form
    
    json_data = json.loads(data)
    data_input_string = json_data['input_string']
    print(data_input_string)

    output = prediction_return(data_input_string)
    for item in output:
        op = item
    
    return json.dumps({'output': op})

if __name__=='__main__':
        port = int(os.environ.get('PORT', 5000))

        app.run(host= '0.0.0.0' ,port =port, debug = True)


