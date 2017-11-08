#!/bin/bash

cp -vf test.py /tmp
cd /tmp
python2 test.py
rm -vf test.py
cd - 

