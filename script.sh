#!/bin/bash

blender src/input/input.blend --engine BLENDER_EEVEE --background --python src/main.py -t 0
FLASK_APP=src/server.py python3 -m flask run --host "0.0.0.0"
