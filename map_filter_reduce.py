# map example
list1 = [2,3,4,5,6]
double_all_element = list(map(lambda x:x*2,list1))
print(double_all_element)
# filter example
list2 = [12,14,15,17,19,29] 
filter_list2 = list(filter(lambda x:x>15,list2))
print(filter_list2)
# reduce example
from functools import reduce
list3 = [2,3,4,5,6]
sum_num = reduce(lambda x,y:x+y,list3)
print(sum_num)