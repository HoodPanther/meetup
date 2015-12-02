# meetup
ipython notebooks for Nervana's San Diego meetup

## Installation

The notebooks require neon and all its dependencies to be installed (See [here](http://neon.nervanasys.com/docs/latest/user_guide.html#installation) for instructions). After activating the neon environment, (i.e. `. .venv/bin/activate` from the neon directory), install these additional packages:

`pip install ipython jupyter matplotlib`

Make sure you have the [IMDB dataset](https://s3-us-west-1.amazonaws.com/nervana-meetup/labeledTrainData.tsv) (right click and download) in the meetup folder, and run the notebook server

`ipython notebook --ip 0.0.0.0`

which should open a new browser window. 

## Usage

There are two notebooks, *cifar_example.ipynb* and *imdb_example.ipynb* to explore. For an intro to running notebooks, see the [Jupyter](https://jupyter.org) documentation. 
