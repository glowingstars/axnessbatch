import re
def test_patterns(text,patterns=[]):
    for pattern in patterns:
        print()
        print('matching"%s"'%pattern)

    for match in re.finditer(pattern,text):
        s=match.start()
        e=match.end()
    print('%d:%d="%s"'%(s,e,text[s:e]))
if __name__=='__main__':

    test_patterns('This is a prime # 1 example!','[r'\d+']')
