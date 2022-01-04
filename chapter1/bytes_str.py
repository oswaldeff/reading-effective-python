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
#1 variables ordering problem
key = 'my_var'
value = 1.234
formatted = '%-10s = %.2f' % (key, value)
print(formatted) # my_var = 1.23
formatted = '%-10s = %.2f' % (value, key)
print(formatted) # error

#2 readable problem
pantry = [
    ('apple', 1.25),
    ('banana', 2.5),
    ('cherry', 15),
]

'title method'

for i, (item,count) in enumerate(pantry):
    print('#%d: %-10s = %.2f % (i, item, count)') # >>> #0:apple = 1.25     #1:banana = 2.50    #2:cherry = 15.00

for i, (item, count) in enumerate(pantry):
    print('#%d: %-10s = %d % (i+1, item.title(), round(count))') # >>> #1: apple = 1    #2:banana = 2   #3:cherry = 15

#3 using str.format many times, problem occur

#4 
