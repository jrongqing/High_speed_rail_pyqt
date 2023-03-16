from PyQt5 import QtGui
from PyQt5 import QtWidgets

# 图片路径
img_path = "image_path.jpg"
# 设置展示控件
pic_show_label = QtWidgets.QLabel()
# 设置窗口尺寸
pic_show_label.resize(500, 500)
# 加载图片,并自定义图片展示尺寸
image = QtGui.QPixmap(img_path).scaled(400, 400)
# 显示图片
pic_show_label.setPixmap(image)