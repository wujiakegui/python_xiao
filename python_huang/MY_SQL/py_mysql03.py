import pymysql
# 改
def main():
    Sno = int(input('输入要更新的学生的学号：'))
    Sname = input("更新学生姓名：")
    # 建立数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='xiao', db='school', charset='utf8')
    try:
        # 获得游标对象
        with conn.cursor() as cursor:
            # 执行SQL得到结果
            result = cursor.execute('update tb_student set Sname = %s where Sno = %s', (Sname, Sno))
            if result == 1:
                print("更新成功")
            conn.commit()                           # 操作成功执行提交
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()                             # 操作失败执行回滚
    finally:
        conn.close()                                # 关闭连接释放资源

if __name__ == '__main__':
    main()
