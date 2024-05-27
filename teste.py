
# lista = [20,9,3,23,6,55,67,92,77,12,2,39,44]

# num_par = filter(lambda x: x % 2 == 0, lista)

# print('lista : => ',list(num_par))
# for i,item in enumerate(num_par):
#     print((i,item))
    
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# log na base 10
#from math import log10
#print map(log10, nums)
# Dividindo por 3
val_list = map(lambda x: x / 3, nums)
print (list(val_list), nums)
    

    
    
