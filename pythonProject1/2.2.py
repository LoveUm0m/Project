mylist = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
newlist = []
for elem in mylist:
    if elem.isdigit():
        newlist.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        newlist.extend(['"', f'{elem[0]}{int(elem):02}', '"'])
    else:
        newlist.append(elem)

outinfo = ' '.join(newlist)
print(outinfo)