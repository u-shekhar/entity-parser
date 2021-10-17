import spacy
import os
from flask import Flask, render_template, request
from flasgger import Swagger

path = r"C:\Users\ujjwa\Desktop\Capstone\Deploy\NER_Model"
nlp = spacy.load(path)

# Defining the name (will fetch from the actual file name)
app = Flask(__name__)
Swagger(app)

# Defingin the path or url attahced after the local ip
@app.route('/', methods=['GET'])
def get_entities():
    """ Practicing Swagger
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
    doc = nlp(input)
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