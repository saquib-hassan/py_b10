"""Invert a dictionary so that values become keys and keys become values."""

my_family = {
    "Saquib" : 29,
    "Shobnom": 22,
    "Shayan" : 2.4
}

inverted_family = {}

for key in my_family:
    value = my_family[key]
    inverted_family[value] = key

print(inverted_family)