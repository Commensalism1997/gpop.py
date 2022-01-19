import gpop
while True:
    nick = input()
    data = gpop.get_data(nick)
    print(f'''
{nick} stats:
Level: {data.level}
Time played: {data.time}
Levels played: {data.played}
Levels created: {data.created}
Views: {data.views}
G-Coins: {data.coins}
GBobs: {data.gbobs}
''')
