def find_common_participants(first, second, separator = ','):
     union = set(first.split(separator))&set(second.split(separator))
     return sorted(list(union))



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,'|'))