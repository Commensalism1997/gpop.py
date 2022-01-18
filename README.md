# gpop.py
![Version - Prototype](https://img.shields.io/badge/Version-Prototype-red?style=for-the-badge&logo=python)

Module that will help you collect data from gpop.io
# Usage
#### Displaying coins
```python
import gpop
nick = input()
coins = gpop.get_coins(nick)
print(f"{nick} has {coins} coins")
```
Expected Output:
```
Commensalism
Commensalism has 625 coins
```
