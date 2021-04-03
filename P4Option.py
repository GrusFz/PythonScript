import json

with open("./MassageList.json","r") as load_f:
    load_dict = json.load(load_f)
    print(load_dict['cnshaw2031'][1]['param2'])
    clientname = load_dict['cnshaw2031'][1]['param2']
    print(clientname)