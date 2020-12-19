c = open('README.md').read()


def str_cnt(n):
    if n < 10:
        return '0' + str(n)
    return str(n)


def write(fname, content):
    f = open(fname, 'w')
    f.write(content)
    f.close()


cnt = 1

for part in c.split('. ### '):
    if 'Back to Top](#table-of-contents)**' not in part:
        continue
    q = 'JavaScript: ' + part.split('\n')[0] + '?'
    arr = []
    for l in part.split('\n')[1:-3]:
        if len(l) > 0 and l[0:3] == '   ':
            l = l[3:]
        arr.append(l)
    a = '\n'.join(arr)
    a = a.replace('](images/', '](https://7465-test-3c9b5e-books-1301492295.tcb.qcloud.la/images/compress_')
    print 'question:', q
    print 'answer:', a
    print '\n*************************************\n'
    write('q' + str_cnt(cnt) + '.md', q)
    write('a' + str_cnt(cnt) + '.md', a)
    cnt += 1
#     if cnt > 5:
#         break
