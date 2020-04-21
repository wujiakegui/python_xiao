import pymysql
# 增
def main():
    # 建立数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='xiao', db='school', charset='utf8')
    try:
        # 获得游标对象
        with conn.cursor() as cursor:
            # 执行SQL得到结果
            result = cursor.execute('insert into tb_student values("5555","黄奇",1,"1997-10-10","CC")')
            if result == 1:
                print("添加成功")
            conn.commit()                           # 操作成功执行提交
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()                             # 操作失败执行回滚
    finally:
        conn.close()                                # 关闭连接释放资源

if __name__ == '__main__':
    main()
