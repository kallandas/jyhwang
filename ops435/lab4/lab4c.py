#!/usr/bin/env python3
# Author ID: jyhwang
# To create dictionaries, extract data from dictionaries, and to make comparisons between dictionaries.

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    dict = {}
    a = 0
    for key in keys:
        dict[key] = values[a]
        a = a + 1
    return dict
    # Place code here - refer to function specifics in section below

def shared_values(dict1, dict2):
    s3=set(dict1.values()).intersection(set(dict2.values()))
    return s3
    # Place code here - refer to function specifics in section below


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)