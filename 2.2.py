# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
def find_common_participants(first_group: str, second_group: str, separator: str = ","):
    set_first = set(first_group.split(separator))
    set_second = set(second_group.split(separator))

    common_participants = sorted(set_first & set_second)

    return common_participants
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator="|"
)

print(result)