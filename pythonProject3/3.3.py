def thesaurus(*names):
    out = dict()
    for name in names:
        out.setdefault(name[0], [])
        out[name[0]].append(name)
    return  out
print(thesaurus("Иван", "Мария", "Петр", "Илья"))