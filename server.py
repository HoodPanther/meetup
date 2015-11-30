from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    site = """
<a href = http://meetup.nervanasys.com:8888/notebooks/cifar_example.ipynb >Cifar Example</a> <br>
<a href = https://s3-us-west-1.amazonaws.com/nervana-meetup/labeledTrainData.tsv >IMDB Dataset</a> <br>
"""
    return site

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
