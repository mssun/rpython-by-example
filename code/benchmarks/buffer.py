#!/usr/bin/env python
# -*- coding: utf-8 -*-

table = [range(1000) for i in range(1000)]

class a(object):
  def main(self, table):
    _buffer = []
    _buffer_write = _buffer.append
    _buffer_write(u'<table xmlns:py="http://spitfire/">')
    _buffer_write(u'\n')
    for row in table:
      _buffer_write(u'<tr>')
      _buffer_write(u'\n')
      for column in row:
        _buffer_write(u'<td>')
        _buffer_write('%s' % column)
        _buffer_write(u'</td>')
        _buffer_write(u'\n')
      _buffer_write(u'</tr>')
      _buffer_write(u'\n')
    _buffer_write(u'</table>')
    _buffer_write(u'\n')
    return ''.join(_buffer)


if __name__ == '__main__':
    a().main(table)
