users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
att ={'Общее количество':0,'Уникальные посещения':0}
att['Общее количество'] = len(users)
att['Уникальные посещения'] = len(set(users))
print(att)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
