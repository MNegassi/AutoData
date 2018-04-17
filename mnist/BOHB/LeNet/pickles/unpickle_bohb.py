#!/usr/bin/python3
# -*- coding: iso-8859-15 -*-



import pickle
import json


for i in range(1, 6):
    with open("BOHB_mnist_{}.pickle".format(i), "rb") as fh:
        HB_result = pickle.load(fh)

    # save idtoconfig_mapping to json file

    res = HB_result.get_id2config_mapping()

    config_list = []
    for key, value in res.items():
        config_list.append(value["config"])


    print(len(config_list))
    with open("id2config_mapping_{}.json".format(i), "w") as fh:
        json.dump(config_list, fh)


with open("id2config_mapping_{}.json".format(2), "r") as fh:
    print(json.load(fh)[i])



#def remap_keys(mapping):
#    return [{'key':k, 'value': v} for k, v in mapping.items()]
#
#
#for i in range(1, 6):
#    with open("BOHB_mnist_{}.pickle".format(i), "rb") as fh:
#        HB_result = pickle.load(fh)
#
#    # save idtoconfig_mapping to json file
#    with open("id2config_mapping_{}.json".format(i), "w") as fh:
#        json.dump(remap_keys(HB_result.get_id2config_mapping()), fh)
#
#
#    with open("id2config_mapping_{}.json".format(i), "r") as fh:
#        print(json.load(fh)[i]['value']['config'])

#import pickle
#import json
#
#with open("BOHB_cifar10_3.pickle", "rb") as fh:
#    HB_result = pickle.load(fh)
#
## save idtoconfig_mapping to json file
#
#res = HB_result.get_id2config_mapping()
#
#config_list = []
#for key, value in res.items():
#    config_list.append(value["config"])
#
#with open("id2config_mapping.json", "w") as fh:
#    json.dump(config_list, fh)
#
#with open("id2config_mapping.json", "r") as fh:
#    print(json.load(fh)[3])
