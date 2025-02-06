import pymysql


def connect():
    conn = pymysql.connect(host='localhost', user='root', password='prabh@1920', database='employee_erp')
    return conn


if __name__ == "__main__":
    connect()
