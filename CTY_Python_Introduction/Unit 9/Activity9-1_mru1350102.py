HighLevelLang_list = ['Ada', 'Basic', 'C', 'C++', 'Java', 'Python', 'Scratch']
print(HighLevelLang_list)
print(HighLevelLang_list[0])
print(HighLevelLang_list[6])
print(len(HighLevelLang_list))
print("%s is the %dth item in the list" % (HighLevelLang_list[6], len(HighLevelLang_list)))
for count in range(0,7):
    print(HighLevelLang_list[count])
HighLevelLang_list.append("Smalltalk")
print(HighLevelLang_list)
del HighLevelLang_list[1]
print(HighLevelLang_list)
HighLevelLang_list.insert(3, 'ColdFusion')
print(HighLevelLang_list)
moreLang_list = ['C#', 'Cobol', 'Fortran']
HighLevelLang_list = HighLevelLang_list + moreLang_list
print(HighLevelLang_list)
HighLevelLang_list.sort()
print(HighLevelLang_list)
