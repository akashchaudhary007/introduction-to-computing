#1
def perfect_number(n):
sum = 0
for x in range(1, n):
if n % x == 0:
sum += x
return sum == n
print(perfect_number(6))
True
(b) def perfect_number(n):
sum = 0
for x in range(1, n):
if n % x == 0:
sum += x
return sum == n
print(perfect_number(5))
False
#2
def isPalindrome(string):
left_pos = 0
right_pos = len(string) - 1
while right_pos >= left_pos:
if not string[left_pos] == string[right_pos]:
return False
left_pos += 1
right_pos -= 1
return True
print(isPalindrome('aza'))
True
#3
def pascal_triangle(n):
 trow = [1]
 y = [0]
 for x in range(max(n,0)):
 print(trow)
 trow=[l+r for l,r in zip(trow+y, y+trow)]
 return n>=1
pascal_triangle(6)

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
#4
import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
alphaset = set(alphabet)
return alphaset <= set(str1.lower())
print ( ispangram('The quick brown fox jumps over the lazy dog'))
True
#5
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
green-red-black-yellow-white
black-green-red-white-yellow
#6
def student_data(student_id, **kwargs):
print(f'\nStudent ID: {student_id}')
if 'student_name' in kwargs:
print(f"Student Name: $ {kwargs['student_name']}")
if 'student_name' and 'student_class' in kwargs:
print(f"\nStudent Name: $ {kwargs['student_name']}")
print(f"Student Class: $ {kwargs['student_class']}")
student_data(student_id='SV12', student_name='Jean Garner')
student_data(student_id='SV12', student_name='Jean Garner', student_class
='V')
Student ID: SV12
Student Name: $ Jean Garner
Student ID: SV12
Student Name: $ Jean Garner

Student Name: $ Jean Garner
Student Class: $ V