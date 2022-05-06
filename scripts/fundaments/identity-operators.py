# compare operators types

string_01 = str('Hellow')
string_02 = str('Hellow2')

compare_01 = (string_01 is string_01)
print(compare_01)

compare_02 = (string_01 is string_02)
print(compare_02)

compare_03 = (string_01 == string_02)
print(compare_03)

compare_04 = (type(string_01) == type(string_02))
print(compare_04)