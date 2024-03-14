car = {
    "color": "white",
    "doors": 4,
    "year": 2019,
    "engine-size": 1.8,
    "tires": ["x","y","z"],
    "owner": [
        {
        "name": "harjot",
        "age": 20,
        "school": "mv"
        },
        {
            "name": "husnain",
            "age": 19,
            "school": "momo"
        }
    ]
}

key = {
    "a": "?",
    "b": "g",
    "c": "-"
}

pwd = "abc"

encryptedPwd = ""
for i in range(0, len(pwd), 1):
    encryptedPwd = encryptedPwd + key[pwd[i]]

print(encryptedPwd)