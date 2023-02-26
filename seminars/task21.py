# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": "S005"}, {" V ":" S009 "},{" VIII":" S007 "}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

massive = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
           {"VI": "S005"}, {"VII": "S005"}, {" V ": " S009 "}, {" VIII": " S007 "}]

set1 = set()
for i in massive:
    for j in i:
        set1.add(i[j])
print(set1)
# for (k, v) in dictionary.items():
#     print(v)
