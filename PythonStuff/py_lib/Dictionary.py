from pprint import pprint
dictionary_variable = {"Danny": ["Green", "Emerald", "turquoise"],
                       "Jade": {"FavColour": "Teal", "LeastFav": "Red"},
                       "Ensty": "Blue"}

# print(dictionary_variable.keys())
# for i in dictionary_variable.keys():
#     print(dictionary_variable[i])

# for i in dictionary_variable.values():
#     print(i)

print(dictionary_variable["Danny"][2])
print(dictionary_variable["Jade"]["LeastFav"])

pprint(dictionary_variable)