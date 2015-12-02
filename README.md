# meetup

[![Join the chat at https://gitter.im/NervanaSystems/meetup](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/NervanaSystems/meetup?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
ipython notebooks for Nervana's San Diego meetup

## Installation

The notebooks require neon and all its dependencies to be installed (See [here](http://neon.nervanasys.com/docs/latest/user_guide.html#installation) for instructions). After activating the neon environment, (i.e. `. .venv/bin/activate` from the neon directory), install these additional packages:

`pip install ipython jupyter matplotlib`

And git clone this repository. Make sure you have the [IMDB dataset](https://s3-us-west-1.amazonaws.com/nervana-meetup/labeledTrainData.tsv) (right click and download) in the meetup folder. Then `cd` to the meetup reository folder and run the notebook server

`ipython notebook --ip 0.0.0.0`

which should open a new browser window. 

## Usage

There are two notebooks, *cifar_example.ipynb* and *imdb_example.ipynb* to explore. For an intro to running notebooks, see the [Jupyter](https://jupyter.org) documentation. 
