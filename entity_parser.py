from flask import Flask
from flasgger import Swagger
import pickle
import spacy
import os
import warnings
warnings.filterwarnings('ignore')

# Defining the name (will fetch from the actual file name)
app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Running"

if __name__ == "__main__":
    # Use debug only when required. With debug no need to stop the server every time.
    #app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
    # Use Cntl+C to stop the server.