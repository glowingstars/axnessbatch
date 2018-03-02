import re
text=' This is a prime #1 example!'
pattern=r'\d+'
for i in re.finditer(pattern,text):
    s=i.start()
    e=i.end()
    print('found"%s" at %d:%d'%(text[s:e],s,e))




