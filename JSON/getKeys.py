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


def get_key(data, val):
    resultKey = ''
    for k, v in data.items():
        if type(data[k]) == dict:
            return get_key(data[k], val)
        elif type(data[k]) == list:
            for key in data[k]:
                if type(key) == dict:
                    return get_key(key, val)
        elif data[k] == val:
            resultKey = k
            break
    return resultKey


def update_json(data, key, val):
    for k, v in data.items():
        if type(data[k]) == dict:
            update_json(data[k], key, val)
        elif type(data[k]) == list:
            for k in data[k]:
                if type(k) == dict:
                    update_json(k, key, val)
        elif k == key:
            data[k] = val
            break
    return data


# print(get_key(jsonData, 6))
print(update_json(jsonData, 'g', 7))

