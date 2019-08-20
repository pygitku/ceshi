# import re
# print(re.split('a','fkit,fafsfa,asgsg,sdf'))
# pa = re.compile('aas')
# print(pa.match('www.aassf.com',4).span())
# import matplotlib.pyplot as plt
# import matplotlib
# x_data = ['2011','2012','2013','2014','2015','2016','2017']
# y_data = [58000,60200,63000,71000,84000,90500,10700]
# y_data1 = [5800,6020,6300,7100,8400,9050,10700]
# lin1=plt.plot(x_data,y_data,color = 'black',linewidth = 2.0,linestyle='--',label ='噶')
# lin2=plt.plot(x_data,y_data1,color = 'pink',linewidth = 2.0,linestyle='--',label ='大师傅')
# zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")
# zhfont1 = matplotlib.font_manager.FontProperties(fname="SimHei.ttf")
# plt.title("图表 - 测试",fontproperties=zhfont1)
# plt.legend(loc='best' )
# plt.show()
import copy
# li1 = [1, 2, 3]
# print(id(li1))
# li2 = li1.copy()
# li1.append(4)
# print(li1, li2)
# print(id(li1),id(li2))
# v = dict.fromkeys(['k1', 'k2'], [])
# v['k1'].append(66)
# print(v)
# v['k1'] = 777
# print(v)
# print('\n'.join(' '.join(['%s*%s=%s'%(j,i,i*j) for j in range(1,1+i)]) for i in range(1,10)))
# a= [i*i for i in range(1,11)]
# print(type(a))
# print(a)
# print('Hello,%s' % 'Python')
# print('Hello,%d%s%.2f' % (666, 'Python', 9.99))
# class FooParent(object):
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#         print('1111')
#
#     def bar(self, message):
#         print("%s from Parent" % message)
#
#
# class FooChild(FooParent):
#     def __init__(self):
#         # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
#         super(FooChild, self).__init__()
#         print('Child')
#
#     def bar(self, message):
#         # super(FooChild, self).bar(message)
#         print('Child bar fuction')
#         print(self.parent)
#
#
# if __name__ == '__main__':
#     fooChild = FooChild()
#     fooChild.bar('HelloWorld')
# class Foo:
#     def __init__(self,name):
#         self.name=name
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
#
# f1=Foo('sb')
# f1['age']=18
# f1['age1']=19
# del f1.age1
# del f1['age']
# f1['name']='alex'
# print(f1.__dict__)
# class Num:
#     # 普通方法：能用Num调用而不能用实例化对象调用
#     def one():
#         print('1')
#
#     # 实例方法：能用实例化对象调用而不能用Num调用
#     def two(self):
#         print('2')
#
#     # 静态方法：能用Num和实例化对象调用
#     @staticmethod
#     def three():
#         print('3')
#
#     # 类方法：第一个参数cls长什么样不重要，都是指Num类本身，调用时将Num类作为对象隐式地传入方法
#     @classmethod
#     def go(cls):
#         cls.three()
#
#
# Num.one()  # 1
# # Num.two()         #TypeError: two() missing 1 required positional argument: 'self'
# Num.three()  # 3
# Num.go()  # 3
#
# i = Num()
# # i.one()           #TypeError: one() takes 0 positional arguments but 1 was given
# i.two()  # 2
# i.three()  # 3
# i.go()  # 3
# class MyType(type):
# # #     def __call__(self, *args, **kwargs):
# # #         return 'MyType'
# # #
# # #
# # # class Foo(object, metaclass=MyType):
# # #     def __init__(self):
# # #         return 'init'
# # #
# # #     def __new__(cls, *args, **kwargs):
# # #         return cls.__init__(cls)
# # #
# # #     def __call__(self, *args, **kwargs):
# # #         return 'call'
# # #
# # #
# # # obj = Foo()
# # # print(obj)  # MyType
# - 连接
# - 直接连接：
import redis

r = redis.Redis(host='10.211.55.4', port=6379)
r.set('foo', 'Bar')
print
r.get('foo')
# - 连接池：
import redis

pool = redis.ConnectionPool(host='10.211.55.4', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print
r.get('foo')