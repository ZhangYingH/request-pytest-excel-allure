import pytest
import allure
if __name__ == '__main__':
    '''执行并生成allure测试报告'''
    pytest.main(["-s", "-v","--alluredir","./report/result"])#运行输出并在/report/result目录生成json文件
    import subprocess #通过标准库中的subprocess包来fork一个子进程，并运行一个外部程序
    subprocess.call('allure generate report/result -o report/html --clean', shell=True)#读取json文件并生成html报告
    subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html', shell=True)#生成一个本地的服务，并自动打开html报告


    '''
    说明:推荐将ison文件默认生成当前用例所在的目录下面，因为a11ure会默认读取当前目录下生成的ison文件并生成htm1报告
    否则运行用例中a11ure报告中会生成两个测试套件，一个是按当前用例py文件命名的测试套件，另一个是按当前py用例文件所在
    目录名命名的测试套件，但其实是同一个用例文件
    "-v”输出详细信息
    "-s”输出测试函数或者测试方法里面print()打印出的内容
    "--alluredir","./report/result”在目录下生成json文作
    "--clean”存在相同目录则先进行清除
    '''