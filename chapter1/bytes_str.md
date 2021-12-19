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
    