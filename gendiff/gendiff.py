import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    common_keys = data1.keys() & data2.keys()
    first_keys = data1.keys() - data2.keys()
    second_keys = data2.keys() - data1.keys()
    result = ['{', ]
    for key in common_keys:
        if data1[key] == data2[key]:
            result.append('   ' + key + ': ' + str(data1[key]).lower())
        else:
            result.append(' + ' + key + ': ' + str(data1[key]).lower())
            result.append(' - ' + key + ': ' + str(data2[key]).lower())
    for key in first_keys:
        result.append(' - ' + key + ': ' + str(data1[key]).lower())
    for key in second_keys:
        result.append(' + ' + key + ': ' + str(data2[key]).lower())
    result.append('}')
    answer = str('')
    for i in result:
        answer = answer + i + '\n'
    return answer
