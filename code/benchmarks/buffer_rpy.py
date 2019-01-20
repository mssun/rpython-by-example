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
        _buffer_write(u'%d' % column)
        _buffer_write(u'</td>')
        _buffer_write(u'\n')
      _buffer_write(u'</tr>')
      _buffer_write(u'\n')
    _buffer_write(u'</table>')
    _buffer_write(u'\n')
    return u''.join(_buffer)

if __name__ == '__main__':
    import sys
    table = [range(int(sys.argv[1])) for i in range(int(sys.argv[1]))]
    a().main(table)

def entry_point(argv):
     table = [range(int(argv[1])) for i in range(int(argv[1]))]
     a().main(table)
     return 0

def target(*args):
    return entry_point, None
