# coding=utf-8
"""sqlite3 """
from __future__ import unicode_literals

import sys
import sqlite3

reload(sys)

sys.setdefaultencoding('utf-8')

cx = sqlite3.connect("test.db")

cu = cx.cursor()

# cu.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")

# 插入两行数据
# for t in[(10, 10, 'abc2', 'Yu'), (11, 20, 'cba2', 'Xu')]:
#     cx.execute("insert into catalog values (?,?,?,?)", t)


# cx.commit()



cu.execute("select * from catalog")

print cu.fetchall()[0][1]