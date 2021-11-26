from itertools import product
a = input()
b = input()

a_list = []
b_list= []
a_list = a.split()
map_object = map(int, a_list)
list_a = list(map_object)

b_list = b.split()
map_object = map(int, b_list)
list_b = list(map_object)
list_prod = list(product(list_a,list_b))
list_out = ''
for i in list_prod:
    list_out = list_out + str(i) +' '

print(list_out)
