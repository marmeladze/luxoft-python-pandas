from flask import Flask
import pandas as pd
from iris_utils import *
from collatz import collatz_sequence_generator_from as seq_gen, find_longest_chain_upto as flcu

app = Flask(__name__)


@app.before_first_request
def download_file():
    download_iris_collection() if data_file_does_not_exist() else None

@app.route("/sequence/elem/<int:n>")
def generate_sequence(n):
    if n < 1:
        return "0 is not an option"
    resp = f"Starting from {n}\n"
    resp += "->".join(f'{int(c)}' for c in seq_gen(n))
    resp += "\n"
    return resp

@app.route("/sequence/longest/<int:n>")
def longest_chain_before(n):
    if n < 1:
        return "0 is not an option"
    value, seq = flcu(n)
    resp = f"Longest chain up to {n}\n" 
    resp += f"Starting from: {str(value)}\n"
    resp += f"Sequence: {str(seq)}\n"
    resp += f"Length: {len(seq)}\n"
    resp += "\n"
    return resp


@app.route("/iris/group/sepal_length/<float:mx>")
def sepal_length_under(mx):
    df = pd.read_csv('collection.csv')
    resp = ""
    resp += f"{df[df['sepal_length'] < mx].groupby('species')['sepal_length'].count()}"
    resp += "\n"
    return resp


@app.route("/iris/describe")
def general_info():
    df = pd.read_csv('collection.csv')
    resp = ""
    resp += f"General:\n {df.describe()}\n"
    resp += "Grouped stats:\n"
    resp += f"Grouped maxes:\n {df.groupby('species').max()}\n"
    resp += f"Grouped mins:\n {df.groupby('species').min()}\n"
    resp += f"Grouped mean:\n {df.groupby('species').mean()}\n"
    resp += f"Grouped median:\n {df.groupby('species').median()}\n"

    resp += "By props: \n"
    resp += f"Sepal length:\n {df.groupby('species').sepal_length.describe()}\n"
    resp += f"Sepal width:\n {df.groupby('species').sepal_width.describe()}\n"
    resp += f"Petal length:\n {df.groupby('species').petal_length.describe()}\n"
    resp += f"Petal width:\n {df.groupby('species').petal_width.describe()}\n"
    resp += "\n"
    return resp


@app.route("/")
def hello_world():
    return """
    Generate collatz sequence starting n:
    \t curl http://127.0.0.1:5000/sequence/elem/<int:n>
    \t Example: \n\tcurl http://127.0.0.1:5000/sequence/elem/119

    Longest sequence under <n>:
    \t curl http://127.0.0.1:5000/sequence/longest/<int:n>
    \t Example: \n\tcurl http://127.0.0.1:5000/sequence/longest/500
    """
