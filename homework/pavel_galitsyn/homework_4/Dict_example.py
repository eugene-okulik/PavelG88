my_dict = {
    'tuple': ('a', 'b', 'c', 'd', 'e'),
    'list': [1, 2, 3, 4, 5],
    'set': {'a1', 'a2', 'a3', 'a4', 'a5'},
    'dict': {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}}

print(my_dict['tuple'][-1])

my_dict['list'].append(6)
print(my_dict['list'])

my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = 'from mars'
print(my_dict['dict'])

my_dict['dict'].pop('key1')
print(my_dict['dict'])

my_dict['set'].add('a6')
print(my_dict['set'])

my_dict['set'].remove('a1')
print(my_dict['set'])

print(my_dict)
