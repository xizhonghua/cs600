#!/usr/bin/env python
import sys

"""
  TM that decides the language L = {a^nb^nc^n|n>=0}

"""


class TM_abc():

  def __init__(self):

    return

  """
  Get the char in head position
  """

  def get(self):
    return self.x[self.head]

  def move(self, d, val=None):
    if val is not None:
      self.x[self.head] = val

    # markers = [' ' for i in range(0, len(self.x))]
    # markers[self.head] = '^'

    # print ''.join(self.x), self.state
    # print ''.join(markers)

    if d == 'L':
      self.head -= 1
    if d == 'R':
      self.head += 1

  def q_0(self):
    self.state = 0
    c = self.get()
    if c == ' ':
      return self.q_acc()
    elif c == 'x':
      self.move('R')
      return self.q_0()
    elif c == 'a':
      self.move('R', 'x')
      return self.q_1()
    else:
      return self.q_rej()

  def q_1(self):
    self.state = 1
    c = self.get()
    if c == 'a' or c == 'x':
      self.move('R')
      return self.q_1()
    elif c == 'b':
      self.move('R', 'x')
      return self.q_2()
    else:
      return self.q_rej()

  def q_2(self):
    self.state = 2
    c = self.get()
    if c == 'b' or c == 'x':
      self.move('R')
      return self.q_2()
    elif c == 'c':
      self.move('R', 'x')
      return self.q_3()
    else:
      return self.q_rej()

  def q_3(self):
    self.state = 3
    c = self.get()
    if c == ' ':
      self.move('L')
      return self.q_5()
    elif c == 'c':
      self.move('R')
      return self.q_4()
    else:
      self.move('R')
      return self.q_rej()

  def q_4(self):
    self.state = 4
    c = self.get()
    if c == 'c':
      self.move('R')
      return self.q_4()
    elif c == ' ':
      self.move('L')
      return self.q_5()
    else:
      self.move('R')
      return self.q_rej()

  def q_5(self):
    self.state = 5
    c = self.get()
    if c == ' ':
      self.move('R')
      return self.q_0()
    else:
      self.move('L')
      return self.q_5()

  def q_acc(self):
    self.state = 'acc'
    return 'accept'

  def q_rej(self):
    self.state = 'rej'
    return 'reject'

  def run(self, x):
    """
    >>> TM_abc().run('abc')
    'accept'
    >>> TM_abc().run('aaabbbccc')
    'accept'
    >>> TM_abc().run('abcc')
    'reject'
    >>> TM_abc().run('ac')
    'reject'
    >>> TM_abc().run('cabc')
    'reject'
    >>> TM_abc().run('aabbc')
    'reject'
    """
    self.x = list(' ' + x + ' ')
    self.head = 1
    return self.q_0()


if __name__ == '__main__':
  if len(sys.argv) == 1:
    print 'Usage: %s x' % (sys.argv[0])
  else:
    tm = TM_abc()
    print sys.argv[1]
    print tm.run(sys.argv[1])
