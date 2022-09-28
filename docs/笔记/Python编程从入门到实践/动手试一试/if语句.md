## 5-3 外星人颜色
```python
alien_color = 'green' 
if alien_color == 'green': 
	print("You just earned 5 points!")
```
## 5-4 外星人颜色2
```python
alien_color = 'yellow' 
if alien_color == 'green': 
	print("You just earned 5 points!") 
else:
	print("You just earned 10 points!")
```
## 5-5 外星人颜色3
```python
alien_color = 'red' 
if alien_color == 'green': 
	print("You just earned 5 points!") 
elif alien_color == 'yellow': 
	print("You just earned 10 points!") 
else: 
	print("You just earned 15 points!")
```
## 5-6 人生不同阶段
```python
age = 17 
if age < 2: 
	print("You're a baby!") 
elif age < 4: 
	print("You're a toddler!") 
elif age < 13: 
	print("You're a kid!")
elif age < 20:
	print("You're a teenager!")
elif age < 65: 
	print("You're an adult!") 
else: 
	print("You're an elder!")
```
## 5-7 喜欢的水果
```python
favorite_fruits = ['blueberries', 'salmonberries', 'peaches'] 
if 'bananas' in favorite_fruits:
	print("You really like bananas!")
if 'apples' in favorite_fruits: 
	print("You really like apples!") 
if 'blueberries' in favorite_fruits: 
	print("You really like blueberries!") 
if 'kiwis' in favorite_fruits: 
	print("You really like kiwis!") 
if 'peaches' in favorite_fruits:
	print("You really like peaches!")
```
## 5-8 以特殊方式跟管理员打招呼
```python
usernames = ['eric', 'willie', 'admin', 'erin', 'ever'] 
for username in usernames: 
	if username == 'admin': 
		print("Hello admin, would you like to see a status report?") 
	else:
		print(f"Hello {username}, thank you for loggin in again!")
```
## 5-9 处理没有用户的情形
```python
usernames = [] 
if usernames: 
	for username in usernames: 
		if username == 'admin': 
			print("Hello admin, would you like to see a status report?") 
		else:
			 print(f"Hello {username}, thank you for loggin in again!") 
else:
	print("We need to find some users!")
```
## 5-10 检查用户名
```python
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
	if new_user.lower() in current_users_lower: 
		print(f"Sorry {new_user}, that name is taken.")
	else:
		print(f"Great, {new_user} is still available.")
```
## 5-11 序数
```python
numbers = list(range(1,10))
for number in numbers: 
	if number == 1:
		print("1st") 
	elif number == 2:
		print("2nd") 
	elif number == 3: 
		print("3rd") 
	else:
		print(f"{number}th")
```