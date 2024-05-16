my_list = ['apple', 'banana', 'orange', 'kiwi', 'grape']
print('List:', my_list)
print('First element:', my_list[0])
print('Last element:', my_list[-1])
print('Sublist:', my_list[2:4])
my_list[2] = 'mandarin'
print('Modified list:', my_list)
print()

my_dict = {'apple': 'яблоко',
           'banana': 'банан',
           'orange': 'апельсин',
           'kiwi': 'киви'}
print('Dictionary:', my_dict)
print('Translation:', my_dict['apple'])
my_dict['apple'] = ['яблоко', 'красное']
my_dict['grape'] = 'виноград'
print('Modified dictionary:', my_dict)
