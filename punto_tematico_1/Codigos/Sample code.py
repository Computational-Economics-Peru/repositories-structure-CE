dictionary = {'test':{1,3}, 'test2':{2}, 'test3':{2,3}}
key_list = list(dictionary)
print(key_list)
keys_of_interest = ['test2', 'test3']

for key in keys_of_interest:
    print('key: {}, index: {}'.format(key, key_list.index(key)))
