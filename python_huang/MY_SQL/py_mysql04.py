import pymysql
# 查
def main():
    # 建立数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='xiao', db='school', charset='utf8')
    try:
        # 获得游标对象
        with conn.cursor() as cursor:
            # 执行SQL得到结果
            result = cursor.execute("select Sno,Sname,Ssex,Sbirth,Sdept from tb_student")
            print(cursor.fetchone())
            print(cursor.fetchmany(2))
            print(cursor.fetchall())
            # for row in cursor.fetchall():
            #     print(f'学号：{row[0]}')
            #     print(f'姓名：{row[1]}')
            #     print(f'性别：{row[2]}')
            #     print(f'出生日期：{row[3]}')
            #     print(f'所在学院：{row[4]}')
            #     print('*'*50)
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()                             # 操作失败执行回滚
    finally:
        conn.close()                                # 关闭连接释放资源

if __name__ == '__main__':
    main()
