#!/usr/bin/python

import abc

class I():
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def add(self, x ,y):
    return

class A(I):
    def add(self, x ,y):
        return x + y

class B(I):
    def add(self, x,y):
        return x + y + x + y

a = A()
b = B()

out1 = a.add(5,6)
out2 = b.add(5,6)

print out1
print out2

