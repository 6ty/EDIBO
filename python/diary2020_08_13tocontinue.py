ser@epk428-1:~$ pwd
/home/user
user@epk428-1:~$ ls
 Desktop     Downloads   Music      Public      Videos
 Documents   EDIBO       Pictures   Templates  'VirtualBox VMs'
user@epk428-1:~$ cd EDIBO
user@epk428-1:~/EDIBO$ ls
 11.08.202.txt   git-upload              mans_pirmais_skripts.sh  'SHELL$'
 ABC             h.dat                   Pyth.dat                  test1.py
 DEF             history_20200807a.txt   python                    test1.Python
 EDIBO           history_20200812a.txt   Pyth.png                  test.sh
 G.dat           history_20200812c.txt   README.md                 timetest.py
user@epk428-1:~/EDIBO$ 
user@epk428-1:~/EDIBO$ 
user@epk428-1:~/EDIBO$ cd python
user@epk428-1:~/EDIBO/python$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> fruit = `banana`
  File "<stdin>", line 1
    fruit = `banana`
            ^
SyntaxError: invalid syntax
>>> fruit = 'banana'
>>> fruit = 'watermellone'
>>> letter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'letter' is not defined
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[0]
>>> letter = fruit[1]
>>> letter = fruit[2]
>>> print(letter)
t
>>> fruit = 'banana'
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers
>>> fruit[0]+fruit[1]+fruit[2]
'ban'
>>> fruit = 'banana'
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print last
  File "<stdin>", line 1
    print last
             ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(last)?
>>> print (last)
a
>>> numbers.append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'numbers' is not defined
>>> numbers = []
>>> len(numbers)
0
>>> numbers.append(1)
>>> len(numbers)
1
>>> numurs.append(55)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'numurs' is not defined
>>> len(numbers)
1
>>> numbers
[1]
>>> numbers.append(55)
>>> len(numbers)
2
>>> numbers
[1, 55]
>>> vaardi = ['a','ab','abc']
>>> vaardi
['a', 'ab', 'abc']
>>> vaardu_garumi = []
>>> vaardu_garumi.append(len(vaardi[0]))
>>> vaardu_garumi.append(len(vaardi[1]))
>>> 
>>> vaardu_garumi.append(len(vaardi[2]))
>>> vaardu_garumi
[1, 2, 3]
>>> typpe(vaardi)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'typpe' is not defined
>>> type(vaardi)
<class 'list'>
>>> vaardi = ['a','ab','abc',10]
>>> vaardi
['a', 'ab', 'abc', 10]
>>> index = 0
>>> while index < len(fruit):
...     letter = fruit[index] 
...     print(letter) 
...     index = index + 1
... 
b
a
n
a
n
a
>>> for char in fruit:
... print(char)
  File "<stdin>", line 2
    print(char)
        ^
IndentationError: expected an indented block
>>> for char in fruit:
...     print(char)
... 
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(6:12])
  File "<stdin>", line 1
    print(6:12])
           ^
SyntaxError: invalid syntax
>>> print(s[6:12])
Python
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> 

