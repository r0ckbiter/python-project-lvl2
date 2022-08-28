import json


def generate_diff(first_file, second_file):
    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))
    all_keys = data1.keys() | data2.keys()
    all_keys = sorted(all_keys)
    string = '{' + '\n'
    for key in all_keys:
        if key in data1 and key not in data2:
            string = string + '  - ' + key + ': ' + str(data1[key]) + '\n'
        elif key in data2 and key not in data1:
            string = string + '  + ' + key + ': ' + str(data2[key]) + '\n'
        else:
            if data1[key] == data2[key]:
                string = string + '    ' + key + ': ' + str(data1[key]) + '\n'
            else:
                string = string + '  - ' + key + ': ' + str(data1[key]) + '\n'
                string = string + '  + ' + key + ': ' + str(data2[key]) + '\n'
    string = string + '}'
    string = string.replace('True', 'true')
    string = string.replace('False', 'false')
    return string
