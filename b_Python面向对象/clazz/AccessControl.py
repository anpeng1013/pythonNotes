# -*- coding = utf-8 -*-
# @Time : 2022/11/21 17:49
# @Author : anpeng
# @File : AccessControl.py
# @Software : PyCharm

class BaseClass(object):
    public = 'this is a public attribute'
    __private = 'this is a private attribute.'
    _protected = 'this is a protected attribute '

    def call_arbitrarily_permission(self):
        print(self.public, self._protected, self.__private)

class SubClass(BaseClass):
    pass
