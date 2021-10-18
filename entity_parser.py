from flask import Flask, request
from flasgger import Swagger
import pickle
import spacy
import os
import warnings
warnings.filterwarnings('ignore')

# Defining the name (will fetch from the actual file name)
app = Flask(__name__)
Swagger(app)

model_path = r"pehla_pehla_model.pkl"
pickled_model = open(model_path,"rb")
parser = pickle.load(pickled_model)

@app.route('/')
def welcome():
    return "Runing! add /apidocs at the url end to go to parser"

# @app.route('/parse', methods=['POST'])
# def get_entities():
#     """ Entity Parser for Grocery Recommender
#     ---
#     parameters:
#      - name: input_string
#        in: query
#        type: string
#        required: true
#     responses:
#        200:
#             description: Entities are 

#     """

#     input_string = request.args.get("input_string")
#     doc = parser(input_string)
#     op = ""
#     for ent in doc.ents :
#         op = op + ent.text + ":" + ent.label_ + ";"

#     return op

if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    #app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
    # Use Cntl+C to stop the server.