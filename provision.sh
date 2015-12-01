#!/bin/bash
cd neon
. .venv/bin/activate
cd ../meetup
ipython notebook --ip 0.0.0.0 --no-browser

