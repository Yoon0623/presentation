"""
1. my_join() 함수 구현 : str1과 str2 문자열을 결합해서 return하는 함수
   def my_join( str1, str2 )

2. my_split() 함수 구현 : str 내용 중 ch를 기준으로 분리하여 List에 저장 후 return하는 함수

   def my_ split( str, ch )
"""


def my_join(str1, str2):
    return str1 + str2


str1 = input('첫번째 문자열 입력 : ')
str2 = input('두번째 문자열 입력 : ')

print(my_join(str1,str2))




###############


def my_split(str,ch) :
    split_list = []
    t = str.split(ch)
    split_list.append(t)
    return split_list

str = input('내용 입력 : ')
ch = input('자를 곳 입력 : ')


print(my_split(str, ch))


###########

import sys

num_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_max(num_list):
    max = sys.float_info.min

    for value in num_list :
        if value > max :
            max = value
    return max



def my_min(num_list):
    min = sys.float_info.max

    for value in num_list :
        if value < min :
            min = value
    return min
          
print(my_max(num_list))
print(my_min(num_list))    

