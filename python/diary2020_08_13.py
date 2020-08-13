user@epk428-1:~$ PS1="$ "
 $ 
$ git clone https://github.com/6ty/EDIBO
Cloning into 'EDIBO'...
remote: Enumerating objects: 134, done.
remote: Counting objects: 100% (134/134), done.
remote: Compressing objects: 100% (94/94), done.
remote: Total 134 (delta 35), reused 52 (delta 10), pack-reused 0
Receiving objects: 100% (134/134), 27.14 KiB | 441.00 KiB/s, done.
Resolving deltas: 100% (35/35), done.
$ ls
 Desktop     Downloads   Music      Public      Videos
 Documents   EDIBO       Pictures   Templates  'VirtualBox VMs'
$ cd EDIBO
$ ls
 11.08.202.txt   git-upload              mans_pirmais_skripts.sh  'SHELL$'
 ABC             h.dat                   Pyth.dat                  test1.py
 DEF             history_20200807a.txt   python                    test1.Python
 EDIBO           history_20200812a.txt   Pyth.png                  test.sh
 G.dat           history_20200812c.txt   README.md                 timetest.py
$ cd python
$ pwd
/home/user/EDIBO/python
$ Python idle &
[1] 3180
$ 
Command 'Python' not found, did you mean:

  command 'jython' from deb jython
  command 'python' from deb python3
  command 'python' from deb python
  command 'python' from deb python-minimal
  command 'cython' from deb cython

Try: apt install <deb name>


[1]+  Exit 127                Python idle
$ pwd
/home/user/EDIBO/python
$ ls
diary_29290812a.py      myhistory.dat
first_python_script.py  second_python_script_like_executable.py
history_20200812b.txt
$ pwd
/home/user/EDIBO/python
$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> a = 10
>>> int
<class 'int'>
>>> a
10
>>> 10 == int
False
>>> type(a)
<class 'int'>
>>> type(a) == int
True
>>> type(a) == 10
False
>>> type(a)
<class 'int'>
>>> type(a) == int
True
>>> if type(a) == int:
... print("labi")
  File "<stdin>", line 2
    print("labi")
        ^
IndentationError: expected an indented block
>>> print("labi")
labi
>>> if type(a) == int:
... print("labi")
  File "<stdin>", line 2
    print("labi")
        ^
IndentationError: expected an indented block
>>> if type(a) == int:
... print("labi")
  File "<stdin>", line 2
    print("labi")
        ^
IndentationError: expected an indented block
>>> if type(a) == int:
...     if type(a) == int:
... if type(a) == int(:
  File "<stdin>", line 3
    if type(a) == int(:
    ^
IndentationError: expected an indented block
>>> if type(a) == int:
...     print("labi")  
... else:
...     print("slikti")
... 
labi
>>> a=5.5
>>> if type(a) = int: 
  File "<stdin>", line 1
    if type(a) = int: 
               ^
SyntaxError: invalid syntax
>>> if type(a) = int:
  File "<stdin>", line 1
    if type(a) = int:
               ^
SyntaxError: invalid syntax
>>> if type(a) = int:
  File "<stdin>", line 1
    if type(a) = int:
               ^
SyntaxError: invalid syntax
>>> if type(a) = int:
  File "<stdin>", line 1
    if type(a) = int:
               ^
SyntaxError: invalid syntax
>>> if type(a) == int:
...     print("labi") 
... else:
...     print("slikti")
... 
slikti
>>> if type(a) == int:
...     print("labi")
... elif type(a) == float:
...     print("arī labi") 
... else:
...     print("slikti")
... 
arī labi
>>> if type(a) == int:
...     print("labi") 
... elif type(a) == float:
...     print("arī labi") 
... elif type(a) == int:
...     print 
... 
[1]+  Stopped                 python
$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> history
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'history' is not defined
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
$ history
    1  VirtualBox --startvm XP
    2  quartus
    3  PS1="$ "
    4  git clone https://github.com/6ty/EDIBO
    5  ls
    6  cd EDIBO
    7  ls
    8  cd python
    9  pwd
   10  Python idle &
   11  pwd
   12  ls
   13  pwd
   14  python
   15  history
$ python
Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a =10
>>> type(a\)
  File "<stdin>", line 1
    type(a\)
           ^
SyntaxError: unexpected character after line continuation character
>>> type(a)
<class 'int'>
>>> a
10
>>> if type(a) == int:
...     print("labi") 
... elif type(a) == float:
... print("arī labi") 
  File "<stdin>", line 4
    print("arī labi") 
        ^
IndentationError: expected an indented block
>>> if type(a) == int:
...     print("labi") 
... elif type(a) == float:
...     print("arī labi") 
... elif type(a) == int:
...     print("ir jau labi - bet šo tekstu neviens nekad neredzēs") 
... else:
...     print("slikti")
... 
labi
>>> 

