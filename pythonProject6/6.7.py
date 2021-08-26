with open('bakery.csv', 'w') as f:
    f.write('5978,5\n8914,3\n7879,1\n1573,7')

import sys

editid, new_val = sys.argv[1:]
with open('bakery.csv', 'r+') as f:
    tmp = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(f, 1):

        if i == int(editid):
            tmp.write(f'{new_val}\n')
            change = True
        else:
            tmp.write(line)
    if not change:
        exit('error')

    tmp.seek(0)

    f.truncate(0)
    for line in tmp:
        f.write(line)
    tmp.close()