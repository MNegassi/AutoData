#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import pickle


with open("random_mnist_0.pickle", "rb") as f:
    print(pickle.load(f))
