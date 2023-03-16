#导入库
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.Qt import *
import pymysql
import time

#导入页面
from pre_login import Ui_MainWindow_pre
from create import Ui_MainWindow_create
from login import Ui_MainWindow_login
from check import Ui_MainWindow_check
from history import Ui_MainWindow_history

#导入图片数据库函数
from picture_database import write_pic2mysql
localtime = time.asctime(time.localtime(time.time()))
global operator_id
global jpg
operator_id = ""
#导入算法函数
sys.path.append(r"C:\Users\十一\Desktop\srp\nest-detect")
# from detect.py import detect()


#主页面（初始页面）
class pre_window(QMainWindow, Ui_MainWindow_pre):
    switch_create = QtCore.pyqtSignal()  # 跳转信号
    switch_login = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(pre_window, self).__init__()
        self.setupUi(self)
        self.pushButton_exit.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_creat.clicked.connect(lambda :self.goCreate())
        self.pushButton_login.clicked.connect(lambda :self.goLogin())
        self.setFixedSize(750, 500)


        #按钮测试：
        self.pushButton_login.clicked.connect(lambda :self.test())
    def goCreate(self):
        self.switch_create.emit()
    def goLogin(self):
        self.switch_login.emit()
    def test(self):
        print('the button is clicked')


#新用户页面
class create_window(QMainWindow, Ui_MainWindow_create):
    def __init__(self):
        super(create_window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 450)
        # self.pushButton.clicked.connect(lambda :self.creat_button())


#登陆页面
class login_window(QMainWindow, Ui_MainWindow_login):
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(800, 450)
    #     self.pushButton.clicked.connect(lambda :self.show_check())
    #
    # def show_check(self):
    #     checkWindow = check_window()
    #     checkWindow.show()
    #     self.close()


#检测页面，检测铁轨异物
class check_window(QMainWindow, Ui_MainWindow_check):
    def __init__(self):
        super(check_window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1021, 643)
        self.pushButton_in.clicked.connect(lambda :self.openimage())
        self.pushButton_run.clicked.connect(lambda :self.run_button())

        #设定外部参数
        self.imgName = ''
        self.imgType = ''

        # 信号槽链接显示子窗口槽函数
    def openimage(self):
        global jpg
        self.imgName, self.imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")  # 在电脑上加代码
        jpg = QtGui.QPixmap(self.imgName)#.scaled(self.label_in.width(), self.label_in.height())
        print('imgName: ',self.imgName,' imageType: ',self.imgType)
        self.label_in.setPixmap(jpg)
        self.label_in.setScaledContents(True)

    #检测按钮点击事件
    def run_button(self):
        global jpg
        global operator_id
        path = self.imgName
        my_config = {'host': 'localhost', 'port': 3306, 'user': 'root',
                     'password': '000000', 'db': 'images'}
        write_pic2mysql(path, my_config,operator_id)
        #jpg = QtGui.QPixmap(self.imgName)  # .scaled(self.label_in.width(), self.label_in.height())
        jpg = QtGui.QPixmap(r"C:\Users\十一\Desktop\srp\result\002502.jpg")
        time.sleep(5)
        print('imgName: ', self.imgName, ' imageType: ', self.imgType)
        self.label_out.setPixmap(jpg)
        self.label_out.setScaledContents(True)



#历史记录页面
class history_window(QMainWindow, Ui_MainWindow_history):
    def __init__(self):
        super(history_window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1022, 727)
        self.pushButton_qurey.clicked.connect(lambda :self.show_history_data())
        self.pushButton_exit.clicked.connect(QCoreApplication.instance().quit)

    def show_history_data(self):
        conn = pymysql.connect(host='localhost', user='root', passwd='000000', db='images', port=3306,
                               charset='utf8')  # port必须写int类型,MySQL的默认端口为3306. charset必须写utf8
        cur = conn.cursor()
        sql = "SELECT * FROM history_img"
        # print("连接成功")
        cur.execute(sql)
        result = cur.fetchall()  # 获得所有记录
        # print(result) t
        row = cur.rowcount
        vol = len(result[0])
        cur.close()
        conn.close()
        table = self.tableWidget
        table.setRowCount(row)
        table.setColumnCount(vol)
        table.setHorizontalHeaderLabels(['Name', 'Date', 'Operator_ID'])
        for i in range(row):
            for j in range(vol):
                data = QTableWidgetItem(str(result[i][j]))
                table.setItem(i, j, data)


#控制器
class Controller:
    def __init__(self):
        pass
    #跳转到main窗口
    def show_main(self):
        self.main = pre_window()
        #点击跳转创建账号页面
        self.main.switch_create.connect(self.show_create)
        #点击跳转登录页面
        self.main.switch_login.connect(self.show_login)
        self.main.show()

    #show creste 页面
    def show_create(self):
        self.create = create_window()
        self.login = login_window()
        self.main.close()
        self.create.show()
        #点击跳转登陆页面
        self.create.pushButton.clicked.connect(lambda :self.creat_button())

    #show login 页面
    def show_login(self):
        self.login = login_window()
        self.main.close()
        self.login.show()
        #点击跳转检测页面
        self.login.pushButton.clicked.connect(lambda :self.login_button())

    #新建账号后跳转到 main 页面
    def show_again(self):
        self.create = create_window()
        self.login = login_window()
        self.login.show()
        self.create.close()
        #创建账号后跳转检测页面
        self.login.pushButton.clicked.connect(lambda: self.login_button())

    #登陆后 show 图片检测页面
    def show_check(self):
        self.login = login_window()
        self.check = check_window()
        self.check.show()
        self.login.close()
        #点击历史查询按钮
        self.check.pushButton_history.clicked.connect(lambda :self.show_history())

    #登录账号点击事务
    def login_button(self):
        global operator_id
        print('login button clicked')
        # 用户id
        user_id = self.login.lineEdit.text()
        operator_id = user_id
        # 用户密码
        user_psw = self.login.lineEdit_2.text()
        if check_psw('user','users',user_id,user_psw) == 0:
            #用户名不存在
            self.show_message_user_id_wrong()
        elif check_psw('user','users',user_id,user_psw) == -1:
            self.show_message_user_psw_wrong()
        else:
            self.show_check()
    #创建账号点击事务
    def creat_button(self):
        # 新的用户id
        new_id = self.create.lineEdit.text()
        # 新的用户密码
        new_psw_1 = self.create.lineEdit_2.text()
        # 用户密码（重复）
        new_psw_2 = self.create.lineEdit_3.text()


        #账号不重复
        if check_count('user','users',new_id):
            #1.密码正确：
            if new_psw_1 == new_psw_2:
                self.show_again()
                print("无错误发生")

                #判定为无错误发生，进行数据库连接
                conn = pymysql.connect(host='localhost', port=3306, user='root', password='000000', db='user')
                cur = conn.cursor()
                cur.execute("INSERT INTO users VALUES (%s,%s);", (new_id, new_psw_1))
                conn.commit()
                cur.close()
                conn.close()
            #2.密码不正确
            else:
                self.show_message_psw()

        #账号重复
        else:
            self.show_message_id()

    #历史查询点击事务
    def show_history(self):
        self.check = check_window()
        self.history = history_window()
        self.history.show()
        self.check.close()




    def show_message_id(self):
        QtWidgets.QMessageBox.critical(None, "错误", "该账号已被注册")
    def show_message_psw(self):
        QtWidgets.QMessageBox.critical(None, "错误", "请输入相同的密码")
    def show_message_user_id_wrong(self):
        QtWidgets.QMessageBox.critical(None, "错误", "用户名不存在")
    def show_message_user_psw_wrong(self):
        QtWidgets.QMessageBox.critical(None, "错误", "密码不正确")
#账户数据检测函数
# 获取数据库主键为list
def check_count(database, table_name,id):
    #  创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
    host, user, pwd = 'localhost', 'root', '000000'
    conn = pymysql.connect(host=host, user=user, passwd=pwd, db=database, port=3306,
                           charset='utf8')  # port必须写int类型,MySQL的默认端口为3306. charset必须写utf8
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    sql = 'select * from %s ;' % table_name
    cursor.execute(sql)

    # 获取到sql执行的全部结果
    results = cursor.fetchall()
    table_list = []
    for r in results:
        table_list.append(list(r))  # 由于fetchall方法返回的一个元组，需要每一行为列表形式的数据，将其转换为list类型。

    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    count_list = list(table_list)

    id_list = [row[0] for row in count_list]

    #id重复
    if id in id_list:
        return 0
    #id 不重复
    else:
        return 1
#检测账号密码是否正确
def check_psw(database,table_name,id,psw):
    #  创建连接，指定数据库的ip地址，账号、密码、端口号、要操作的数据库、字符集
    host, user, pwd = 'localhost', 'root', '000000'
    conn = pymysql.connect(host=host, user=user, passwd=pwd, db=database, port=3306,
                           charset='utf8')  # port必须写int类型,MySQL的默认端口为3306. charset必须写utf8
    # 创建游标
    cursor = conn.cursor()
    # 执行sql语句
    sql = 'select * from %s ;' % table_name
    cursor.execute(sql)

    # 获取到sql执行的全部结果
    results = cursor.fetchall()
    table_list = []
    for r in results:
        table_list.append(list(r))  # 由于fetchall方法返回的一个元组，需要每一行为列表形式的数据，将其转换为list类型。

    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接

    #设定flag 0：不存在账号     -1：账号密码错误       1：账号密码正确
    flag = 0
    for items in table_list:
        print('items0:', items[0])
        print('items1:', items[1])
        #存在id
        if items[0] == id:

            if items[1] == psw:
                #账号密码正确
                flag = 1
                break
            else:
                #账号密码错误
                flag = -1
    return flag

def write_pic2mysql(path, config,opID):
    """
    读取图片写入数据库
    :param path: 读取的图片的路径
    :param config: 数据库连接配置信息
    :return: None
    """
    filename = path.split('/')[-1]
    print(filename)
    try:
        with open(path, 'rb') as f:
            img = f.read()
    except:
        print('读取失败')
        # sys.exit(1)
        return
    try:
        conn = pymysql.connect(host=config['host'],
                               port=config['port'],
                               user=config['user'],
                               passwd=config['password'],
                               db=config['db'],
                               charset='utf8',
                               use_unicode=True)
        cursor = conn.cursor()
        operator_id = opID

        print(filename,localtime,operator_id)
		# 注意一下这里的 {0} 的引号，可以试一下去掉引号会提醒没有者找到该字段
        #sql = "INSERT INTO history VALUES (%s,%s,%s)"%(str(filename),str(localtime),str(operator_id))
        cursor.execute("INSERT INTO history_img VALUES (%s,%s,%s);" ,(str(filename),str(localtime),str(operator_id)))
        conn.commit()
        cursor.close()
        conn.close()
        print('写入 {} 成功'.format(filename))
    except Exception as e:
        print(e)
        print('写入失败')

#调用主程序
if __name__=="__main__":
    app=QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())
