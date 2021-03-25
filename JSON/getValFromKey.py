from collections import Counter

data = {
    "a": 1,
    "b": 2,
    "c": [{
        "d": 4,
        "e": 5,
        "f": {
            "g": 6
        }
    }]
}


def get_value_from_the_key(jsonData, key):

    global val
    for k, v in jsonData.items():
        if type(jsonData[k]) == dict:
            get_value_from_the_key(jsonData[k], key)
        elif type(jsonData[k]) == list:
            for k in jsonData[k]:
                if type(k) == dict:
                    get_value_from_the_key(k, key)
        elif k == key:
            print('found')
            val = jsonData[k]
            break
    return val


print(get_value_from_the_key(data, 'g'))


#
# def get_count_of_keys(jsonData, key):
#     val = 0
#     for k, v in jsonData.items():
#         if type(jsonData[k]) == dict:
#             get_count_of_keys(jsonData[k], key)
#         elif type(jsonData[k]) == list:
#             for k in jsonData[k]:
#                 if type(k) == dict:
#                     get_count_of_keys(k, key)
#         elif k == key:
#             print('got')
#             val = val +1
#             print(val)
#             break
#
#
# def get_count():
#     counter = Counter([{'a': 1, 'b': 1, 'c': 1}, {'a': 1, 'b': 1, 'c': 1}])
#     print(counter)
#
# get_count()