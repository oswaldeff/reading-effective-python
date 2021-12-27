#-*-coding: utf-8-*-

# bytes type
a = b'h\x65llo' # ASCII code
print(list(a)) # [104, 101, 108, 108, 111]
print(a) # b'hello

# str instance
a = 'a\u0300 propos' # code point
print(list(a))
print(a) # a' propos

# helper function: to str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value # return: str instance
print(repr(to_str(b'foo'))) # 'foo'
print(repr(to_str('bar'))) # 'bar'
print(repr(to_str(b'\xed\x95\x9c'))) # '한'

# helper function:
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
        return value # bytes instance
print(repr(to_bytes(b'foo')))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한글')))

# add bytes to bytes
print(b'one' + b'two')

# add string to string
print('one' + 'two')

# formatting
print(b'red %s' % 'blue') # erorr
print('red %s' % b'blue') # red b'blue'

# when using c style, there are 4 problems
#1
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted) # my_var = 1.23
