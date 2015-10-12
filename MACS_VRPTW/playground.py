__author__ = 'Lada'
# flavor_list=['vanilla','chocolate','pecan','strawberry']
#
# for i, flavor in enumerate(flavor_list):
#     print('%d: %s' %(i+1,flavor))
#

a=1
b=0
try:
    print(a/b)
except ZeroDivisionError:
    print('Error')