# bytes type and str instance
- unicode -> binary: use encode method of 'str'
- binary -> unicode: use decode method of 'bytes'
- generally, system's default encoding method is 'UTF-8' (not always)
- 'unicode sandwich': place at the farthest border of interface, which https://nedbatchelder.com/text/unipain.html (Pro tip #1) is well explained
> unicode sandwich
        bytes
    decode | Library
        Unicode
        Unicode
    encode | Library
        bytes
- These two cases are possible: add bytes to bytes and add string to string (But, It is couldn't to add bytes to string)
- When compare to bytes with bytes and string with string, comparison operator(asser) can be used (couldn't bytes with string)
- use interpolation(f-string) instead of str.format