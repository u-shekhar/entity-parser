import spacy
import os
from flask import Flask, render_template, request
from flasgger import Swagger
import requests
import pickle

model_path = r"pehla_pehla_model.pkl"
pickled_model = open(model_path,"rb")
parser = pickle.load(pickled_model)

# Defining the name (will fetch from the actual file name)
app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Running"
# Defingin the path or url attahced after the local ip
@app.route('/parse', methods=['POST'])
def get_entities():
    """ Entity Parser for Grocery Recommender
    ---
    parameters:
     - name: input_string
       in: query
       type: string
       required: true
    responses:
       200:
            description: Result is

    """

    input = request.args.get("input_string")
    doc = parser(input)
    op = ""
    for ent in doc.ents :
        op = op + ent.text + ":" + ent.label_ + ";"

    return op


if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    #app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
    # Use Cntl+C to stop the server.