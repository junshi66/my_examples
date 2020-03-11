#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

'''
@File       : os_use.py
@ Author:   :zhaosj
@Time       : 2020/3/11 16:13
'''

''' begin now here '''

import os

'''
os.getcwd()
查看当前所在路径
'''
pre_str = "当前路径是:"
current_path = os.getcwd()
print(pre_str + '\t' + current_path)


'''
os.listdir()
列举目录下所有的文件,返回的是列表类型
'''
dirname = '/tmp/'
pre_str = dirname+"目录下的文件:"
#返回的是一个列表类型
print(os.listdir(dirname),type(os.listdir(dirname)))
#遍历列表
for i in os.listdir(dirname):
    print(dirname + i)


'''
os.path.abspath(path)
返回path的绝对路径
'''
pre_str = '当前路径是'
current_path = os.path.abspath(".")
print(pre_str + '\t' + current_path)


'''
os.path.split(path)
将路径分解为(文件夹,文件名),返回的是元组类型。
注意:若路径字符串最后一个字符是,则只有文件夹部分有值,若路径字符串中均无,则只有文件名部分有值,若路径字符串有\且不在最后,则文件夹和文件名都有值,且返回的结果不包括\
'''
print(os.path.split('/tmp/a/b.txt'))
print(os.path.split('/tmp/a/b'))
print(os.path.split('/tmp/a/b.txt,'))
print(os.path.split('C:\\tmp\\a\\b.txt'))

'''
os.path.join(path1,path2,path3...)
将path进行组合，如果包含绝对路径,会将绝对路径删除
'''
print(os.path.join('/tmp','hello.py'))
print(os.path.join('/tmp/a/a.py','/tmp/a/b.py','/tmp/a/c.py'))
##输出结果 /tmp/a/c.py



'''
os.path.dirname(path)
返回path中的目录部分，不包含"\"
'''
print(os.path.dirname('/tmp/a/b/c.py'))

'''
os.path.basename(path)
返回path中的文件名称
'''
print(os.path.basename('/tmp/a/b/c.py'))
print(os.path.basename('c:\\tmp\\a\\b\\c.py')) ##这个的返回结果是c:\tmp\a\b\c.py


'''
os.path.getsize(path)
获取文件的大小，如果是目录返回0
'''

print(os.path.getsize(r'/HiSQL/scripts/git_test/my_examples/py3/os_use.py'))
print(os.path.getsize(r'/HiSQL/scripts/git_test/my_examples/py3')) ##实际返回4096


'''
os.path.exists(path)
判断文件是否存在，如果存在返回True，否则返回False
'''

print(os.path.exists('/HiSQL/scripts/git_test/my_examples/py3/os_use.py'))


'''
os.path.isdir(path)
判断该路径是否为目录
'''
print(os.path.isdir('/HiSQL/scripts/git_test/my_examples/py3'))

'''
os.path.isfile(path)
判断该路径是否为文件
'''
print(os.path.isfile('/HiSQL/scripts/git_test/my_examples/py3/os_use.xpy'))
print(os.path.isfile('/HiSQL/scripts/git_test/my_examples/py3/os_use.py'))
