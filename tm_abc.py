#!/usr/bin/env python
import sys

"""
  TM that decides the language L = {a^nb^nc^n|n>=0}

"""


class TM_abc():

  def __init__(self):

    self.delta = {
        'q_0': {
            ' ': {'next': 'q_acc'},
            'x': {'next': 'q_0', 'move': 'R'},
            'a': {'next': 'q_1', 'move': 'R', 'val': 'x'},
            '*': {'next': 'q_rej'}
        },
        'q_1': {
            'ax': {'next': 'q_1', 'move': 'R'},
            'b': {'next': 'q_2', 'move': 'R', 'val': 'x'},
            '*': {'next': 'q_rej'}
        },
        'q_2': {
            'bx': {'next': 'q_2', 'move': 'R'},
            'c': {'next': 'q_3', 'move': 'R', 'val': 'x'},
            '*': {'next': 'q_rej'}
        },
        'q_3': {
            ' ': {'next': 'q_5', 'move': 'L'},
            'c': {'next': 'q_4', 'move': 'R'},
            '*': {'next': 'q_rej'}
        },
        'q_4': {
            'c': {'next': 'q_4', 'move': 'R'},
            ' ': {'next': 'q_5', 'move': 'L'},
            '*': {'next': 'q_rej'}
        },
        'q_5': {
            ' ': {'next': 'q_0', 'move': 'R'},
            '*': {'next': 'q_5', 'move': 'L'},
        }
    }
    return

  def move(self, d, val=None):
    if val is not None:
      self.x[self.head] = val

    if d == 'L':
      self.head -= 1
    if d == 'R':
      self.head += 1

  def run(self, x):
    """
    >>> TM_abc().run('')
    'accept'
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
    self.state = 'q_0'
    while True:
      if self.state == 'q_acc':
        return 'accept'
      if self.state == 'q_rej':
        return 'reject'

      c = self.x[self.head]

      key = next((x for x in self.delta[self.state] if c in x), '*')

      delta = self.delta[self.state][key]

      d = delta['move'] if 'move' in delta else None
      val = delta['val'] if 'val' in delta else None
      self.move(d, val)
      self.state = delta['next']

    return 'reject'


if __name__ == '__main__':
  if len(sys.argv) == 1:
    print 'Usage: %s x' % (sys.argv[0])
  else:
    tm = TM_abc()
    print sys.argv[1]
    print tm.run(sys.argv[1])
