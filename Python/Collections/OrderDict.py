from collections import OrderedDict
n_items = int(input())
ordered_dictionary = OrderedDict()
for i in range(0, n_items):
    thing = []
    thing = input().split()
    net_price = thing[-1]
    thing.pop()
    item_name = ' '.join(thing)
    ordered_dictionary[item_name] = int(ordered_dictionary.get(item_name, 0))+ int(net_price)

for key, value in ordered_dictionary.items():
    print(key, value)
