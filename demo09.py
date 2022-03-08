#pymysql固定的方法
import pymysql


#1、查询数据库 只支持select  eg "select * from t_user where id = 123"
def query(sql):
    #1、连接数据库  db要操作的数据库
    db = pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="testdb")
    #2、获取游标：获取查询窗口
    cur = db.cursor()
    #3、执行sql语句
    cur.execute(sql)
    #4、收集结果
    res = cur.fetchall()
    #关闭
    db.close()
    return res

# sql = "select * from sc"
# res = query(sql)
# print(res)
    
#修改方法 只支持updata、delete、inset   不支持select  eg"updata/delete/inset"
def commit(sql):
    #1、连接数据库  db要操作的数据库
    db = pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="testdb")
    #2、获取游标：获取查询窗口
    cur = db.cursor()
    #3、执行sql语句
    cur.execute(sql)
    #4、提交修改
    db.commit()
    #关闭
    db.close()
# sql = "UPDATE sc SET score = 80 WHERE sid = 1"
# commit(sql)

