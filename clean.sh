#!/bin/bash 

sudo rm -rvf build dist temp *.egg-info setup.cfg

find . -type f -name '*.pyc' | xargs rm -vf

