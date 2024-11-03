# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep=','):
    participants1 = set(group1.split(sep))
    participants2 = set(group2.split(sep))

    common_participants = participants1.intersection(participants2)
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group,
                                               participants_second_group, sep='|')
print("Общие участники:", common_participants)