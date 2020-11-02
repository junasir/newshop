import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "shop", "123456", "test", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
cursor.execute('select * from test01 order by 商品id')
D=cursor.fetchall()
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print(D)
# print("Database version : %s " % data)

# 关闭数据库连接
db.close()