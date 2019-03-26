# windows下的轻量级Django #
# 1.没有使用书上PostgressSQL,渣渣win10安装报错，改用MySQL #
# 2.本案例mysql账户和密码（root/root）以及项目的超级用户（admin/admin） #
# 3.安装包及其对应版本#

1. django 2.1.7
2. markdown 3.0.1
3. django-filter 2.1.0
4. djangorestframework 3.9.2
5. mysqlclient 1.4.2
6. PyMySQL 0.9.3
 
# 4.在scrum目录下的init.py加入如下代码：

> import pymysql
> 
> pymysql.install_as_MySQLdb()

#5.由于版本变动有点大，部分变量名和方法以及导入方式已替换，建议自己看代码琢磨#
#6.绝大部分代码来自原书《Lightweight Django》Julia Elman and Mark Lavin(O'Reilly),Copyright 2015 Julia Elman and Mark Lavin，978-1-491-94594-0#
#7.如果对你有点用，试着点亮小星星，谢谢！#