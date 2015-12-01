#!/bin/bash

# activate neon virtual env
cd ~/neon
. .venv/bin/activate
cd ~/meetup

# ensure notebooks are read only
chmod u-w cifar_example.ipynb
chmod u-w imdb_example.ipynb

# launch notebook server
ipython notebook --ip 0.0.0.0 --no-browser

