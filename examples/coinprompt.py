import gpop
while True:
    nick = input()
    coins = gpop.get_coins(nick)
    print(f"{nick} has {coins} coins")
