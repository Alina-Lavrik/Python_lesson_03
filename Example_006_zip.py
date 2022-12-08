# Функция zip

'''users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 8]
rus = ['привет', 'зима', 'снег', 'разработчик', 'ДР']

data = list(zip(users, ids, rus))
print(data) # [('user1', 4, 'привет'), ('user2', 5, 'зима'), ('user3', 9, 'снег'), ('user4', 14, 'разработчик'), ('user5', 8, 'ДР')] '''
# Функция enumerate 

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 8]
rus = ['привет', 'зима', 'снег', 'разработчик', 'ДР']

data = list(enumerate(users))
print(data)   # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]

