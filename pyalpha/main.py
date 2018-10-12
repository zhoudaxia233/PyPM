#! /usr/bin/env python3
# coding: utf-8
from .reader import read
from .alpha import Alpha
from .petri_net import PetriNet
from subprocess import check_call
import sys
import os.path

def main():
    argv = sys.argv
    if (len(argv) < 2) or (not os.path.isfile(argv[1])):
        print("Warning: Please indicate a valid file path.")
        return
    log = read(argv[1])
    filename = os.path.splitext(os.path.basename(argv[1]))[0]
    alpha_model = Alpha(log)
    alpha_model.generate_footprint(txtfile="{}_footprint.txt".format(filename))
    pn = PetriNet()
    pn.generate_with_alpha(alpha_model, dotfile="{}.dot".format(filename))
    check_call(["dot", "-Tpng", "{}.dot".format(filename),"-o", "{}.png".format(filename)])
