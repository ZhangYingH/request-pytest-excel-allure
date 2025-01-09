# coding=gbk
import os
import pytest

pytest.main([])

os.system("allure generate ./report/result -o ./report/html --clean")