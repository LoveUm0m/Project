#1

import os

pattern = {project: ['setings', 'mainapp', 'admin']}
for root, folders in pattern():
    if os.path.exsist(root):
        print(root, 'сущесствует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            if os.path.exsist(cut_dir):
                print(cur_dir, 'существует')
            else:
                os.makedirs(cur_dir)


