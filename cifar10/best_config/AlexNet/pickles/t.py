#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import pickle


with open("best_config_cifar10_0.pickle", "rb") as f:
    print(pickle.load(f))
