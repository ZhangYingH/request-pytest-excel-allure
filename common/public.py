import os
os.path.dirname(__file__)#获取当前目录
os.path.dirname(os.path.dirname(__file__))#获取当前目录的上一级目录

#获取指定的目录
def fileDir(data):

    base_path = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path, data)
#获取路径下的文件，调用需要传递两个参数替换，否则使用默认的参数
def filePath(fileDir="data", fileName="data.xls"):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), fileDir,fileName)
    #添加后返回的路径为"E:\HUI\APITest\data\data.xls"
