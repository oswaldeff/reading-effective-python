# bytes type
a = b'h\x65llo' # ASCII code
print(list(a)) # [104, 101, 108, 108, 111]
print(a) # b'hello

# str instance
a = 'a\u0300 propos' # code point
print(list(a))
print(a) # a' propos
