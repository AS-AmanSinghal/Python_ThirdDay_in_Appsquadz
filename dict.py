dict= {'A':4,
              'B':6,
              'C':-2,
              'D':-8}
print(dict.get('A'))

for key, value in dict.items():
    if 4 == value:
        print(key)