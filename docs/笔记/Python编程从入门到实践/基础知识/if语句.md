## 条件测试
每条`if`语句的核心都是一个值为`True or False`的表达式，这种表达式被称为条件测试，根据条件测试的值来确定是否执行`if`后面的代码
### 检查是否相等
大多数条件测试都将一个变量的当前值同特定值比较，简单的条件测试九四检查变量的值是否与特定值相等
```python
>>> cat = 'bmw'
>>> cat == 'bmw'
True
>>> cat == 'audi'
False
```
一个等号是赋值，两个等号是判断
### 检查是否相等时不考虑大小写
一般的时候，因为大小写的值不相等，所以默认大写不等于小写，可以通过大小写转换函数将字符串**临时**转换成全小写或全大写进行比较
```python
>>>car = 'Audi'
>>>car == 'audi'
False
>>>car.lower() == 'audi'
True
```
### 检查不相等
要判断不相等可以使用`!=`，其中的`!`表示不
```python
fequested = 'mushrooms'
if requested != 'anchovies':
	print('Hold the anchovies!')
```
### 检查多个条件
#### 使用and
要使两个条件都为True，就可以使用and，and类似逻辑运算中的**且**
```python
>>>age1 = 22
>>>age2 = 18
>>>age1 >= 21 and age2 >= 21
False
>>>ag1 >=21 and age2 >= 18
True
```
#### 使用or
要是两个条件其中的一个条件为True，可以使用or，or类似逻辑运算中的**或**
```python
>>>age1 = 22
>>>age2 = 18
>>>age1 >= 21 and age2 >= 21
True
>>> age1 = 18
>>>age1 >=21 and age2 >= 21
False
```
### 检查特定值是否包含在列表中
有时候执行操作前必须检查列表中是否包含特定的值
要判断特定的值是否已包含在列表中，可以使用关键字`in`
```pyton
>>>requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>>'mushrooms' in requested_toppings
True
>>>'pepperoni' in requested_toppings
False
```
### 检查特定值是否不包含在列表中
检查特定值是否不包含在列表中可以使用关键字`not in`
```python
>>>banned_users = ['andrew', 'carolina', 'david']
>>>user = 'marie
>>>if user not in banned_users:
>>>	print(user.title() + ", you can post a response if you wish.")
Marie, you can post a response if you wish.
```
### 布尔表达式
布尔值听常用于记录条件
```python
game_active = True
can_edit = False
```
在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式
#### 动手试一试
```
5-1 条件测试：编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的
代码应类似于下面这样：
car = 'subaru' 
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru') 
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi') 
详细研究实际结果，直到你明白了它为何为True或False。创建至少10个测试，且其中结果分别为True和
False的测试都至少有5个。
5-2 更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将
它们加入到conditional_tests.py中。对于下面列出的各种测试，至少编写一个结果为True和False的
测试。
检查两个字符串相等和不等。
使用函数lower()的测试。
检查两个数字相等、不等、大于、小于、大于等于和小于等于。
使用关键字and和or的测试。
测试特定的值是否包含在列表中。
测试特定的值是否未包含在列表中。
```
## if语句
### 简单的if语句
```python
if conditional_test:
	do something
# 在第一行进行判断，倘若判断为True，则执行do something,反之则会忽略do something
```
在`if`语句中，缩进的作用与for循环相同，例如
```python
age = 19
if age >= 18: 
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
```
### if-else 语句
我们经常需要在测试通过时执行一个操作，在没有通过时执行另一个操作
```python
age = 17 
if age >= 18: 
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else: 
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
```
### if-elif-else结构
```python
age = 12 
if age < 4: 
	print("Your admission cost is $0.") 
elif age < 18: 
	print("Your admission cost is $5.") 
else: 
	print("Your admission cost is $10.")
```
### 使用多个elif代码块
```python
age = 12 
if age < 4: 
	price = 0 
elif age < 18: 
	price = 5 
elif age < 65: 
	price = 10 
else: 
	price = 5 
print("Your admission cost is $" + str(price) + ".")
```
### 省略else代码块
Python并不要求if-elif结构后面必须有else代码块
```python
age = 12
if age < 4:
	price = 0
elif age < 18: 
	price = 5 
elif age < 65: 
	price = 10 
elif age >= 65: 
	price = 5 
print("Your admission cost is $" + str(price) + ".")
```
### 测试多个条件
if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况，然而，有时候必须检查你关心的所有条件，在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。在可能有多个条件为True，且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。
```python
requested_toppings = ['mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
	print("Adding mushrooms.") 
if 'pepperoni' in requested_toppings: 
	print("Adding pepperoni.") 
if 'extra cheese' in requested_toppings: 
	print("Adding extra cheese.") 
print("\nFinished making your pizza!")
```
#### 动手试一试
```
5-3 外星人颜色#1：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，并将其设
置为'green'、'yellow'或'red'。
编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输
出）。
5-4 外星人颜色#2：像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
编写这个程序的两个版本，在一个版本中执行if代码块，而在另一个版本中执行else代码块。
5-5 外星人颜色#3：将练习5-4中的if-else结构改为if-elif-else结构。
如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
5-6 人生的不同阶段：设置变量age的值， 再编写一个if-elif-else结构，根据age的值判断处于人生的
哪个阶段。
如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
5-7 喜欢的水果：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if语句，检查列表中是否
包含特定的水果。
将该列表命名为favorite_fruits，并在其中包含三种水果。
编写5条if语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You 
really like bananas!”。
```
## 使用if语句处理列表
### 检查特殊元素
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings: 
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
# 一个简单的for循环，来指出列表中的元素
```

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 
for requested_topping in requested_toppings: 
	if requested_topping == 'green peppers': 
		print("Sorry, we are out of green peppers right now.") 
	else: 
		print("Adding " + requested_topping + ".") 
print("\nFinished making your pizza!")

```
### 确定列表不是空的
```python
requested_toppings = [] 
if requested_toppings: # 判断列表是否为空，为空则走else
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".") 
	print("\nFinished making your pizza!")
else: 
	print("Are you sure you want a plain pizza?")
```
### 使用多个列表
```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
					  'pineapple', 'extra cheese'] 
requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] 
for requested_topping in requested_toppings: 
	if requested_topping in available_toppings: 
		print("Adding " + requested_topping + ".") 
	else: 
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
```
#### 动手试一试
```
5-8 以特殊方式跟管理员打招呼：创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'。想
象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问
候消息。
如果用户名为'admin'，就打印一条特殊的问候消息，如“Hello admin, would you like to see a 
status report?”。
否则，打印一条普通的问候消息，如“Hello Eric, thank you for logging in again”。
5-9 处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if语句，检查用户名列表是否为空。
如果为空，就打印消息“We need to find some users!”。
删除列表中的所有用户名，确定将打印正确的消息。
5-10 检查用户名：按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
创建一个至少包含5个用户名的列表，并将其命名为current_users。
再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表
current_users中。
遍历列表new_users，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指
出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
确保比较时不区分大消息；换句话说，如果用户名'John'已被使用，应拒绝用户名'JOHN'。
5-11 序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。
在一个列表中存储数字1~9。
遍历这个列表。
在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为1st、2nd、3rd、
4th、5th、6th、7th、8th和9th，但每个序数都独占一行。
```