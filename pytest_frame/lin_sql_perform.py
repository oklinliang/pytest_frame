from lin_mysql import UsingMysql

"""
    所有sql均在这里维护
"""
def check_it():
    with UsingMysql() as um:
        um.cursor.execute("SELECT * FROM xxx WHERE xxx = '林亮';")
        data = um.cursor.fetchone()
        # if(data != None):
        #     print(123)
        # else:
        #     print(345)
        return data