# gpop.py
![Version - Prototype](https://img.shields.io/badge/Version-Prototype-red?style=for-the-badge&logo=python)

Module that will help you collect data from gpop.io
# Examples
#### Displaying coins
```python
import gpop
nick = input()
data = gpop.get_data(nick)
print(f"{nick} has {data.coins} coins")
```
Expected Output:
```
Commensalism
Commensalism has 625 coins
```
