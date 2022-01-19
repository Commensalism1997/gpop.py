# gpop.py
![Version - Prototype](https://img.shields.io/badge/Version-Prototype-red?style=for-the-badge&logo=python)

Module that will help you collect data from gpop.io
# Usage
#### `GPopUserData`
**NOTE**: all fields are `str`. Use `int()` to convert it to numbers
A namedtuple class that contains user's data
Fields:
- level: Level
- time: Total time played
- played: Levels played
- created: Levels created
- views: Views
- coins: GShop coins
- gbobs: Number of GBobs
#### `get_data(user : str) -> GPopUserData`
Collects data of an user and returns GPopUserData with it
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