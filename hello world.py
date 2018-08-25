#coding=utf-8
message = 'HELLO'

print(message.lower())

message_1 = 'python'

print(message.title())

message = 'hello pyhton world!'
print (message.upper())

new_message = message.upper() +'     '+ message_1.title()
print new_message


message_2 = ' hello world forever! '
print (message_2.rstrip())

print(2+3,2-1,2*4,8/1,4**4,0.1*0.2,)

age = 30
message_3 = 'happy ' + str(age) + 'rd birthday!'
print (message_3.upper())

print(3.0/2)
print(5+3)
print(2*4)
print(16/2)
print(10-2)

number=7    #存储数字7到变量中
message_4 = 'my favorite number is:' + str(number)
print(message_4)


name = ['jack','mary','tom','yang']    #列表学习
print(name)
print(name[0])  #列表的索引从0开始
print(name[3].title())
print(name[-1])
print(name[-2].upper().lower())
print 'my name is '+name[0].title() +' how are you'

name[0] = 'frank'       #修改列表元素
print(name)
name.append('jay')      #在列表末尾增加元素
name.append('jarry')
print(name)


name.insert(0,'sam')     #在列表中插入元素
print(name)

del name[0]             #使用del删除列表中的元素
print(name)

pop_name = name.pop()       #使用pop删除列表中元素
print(pop_name)
print(name)

name.pop(-1)
print(name)

name.remove('tom')      #使用remove直接删除元素
print(name)


name.sort()             #永久改变列表元素顺序.sort()方法
print(name)

cars = ['audi','benz','bmw','toyota','honda']

print(sorted(cars,reverse=True))            #临时改变列表顺序函数：sorted
print(cars)

cars.reverse()              #倒着打印列表，注意reverse()方法不是按字母顺序反转列表，而是反转列表元素的排列顺序
print(cars)

print(len(cars))   #确定列表的长度


for car in cars:            #遍历列表中的每个元素
    print(car)

for car in cars:
    print('this is nice car: '+ car)
    print('i want to buy this: '+car+'\n')
print ('where is your money?'+'\n')


for num in range(1,5):              #创建数字列表
    print(num)


number = list(range(1,5))             #使用range()创建数字列表
print(number)

number = list(range(1,11,2))            #指定数字列表输出的不步长
print(number)


result = []
for num_1 in range(1,11):
    num_2 = num_1**2
    result.append(num_2)
print(result)

result = []
for num_1 in range(1,11):
    result.append(num_1**2)
print(result)


max_result = max(result)                #对列表进行统计计算，列表中的最大值、最小值、求和
print(max_result)

min_result = min(result)
print(min_result)

sum_result = sum(result)
print(sum_result)


result = [value**2 for value in range(1,11)]            #列表解析式
print(result)

cars = ['audi','benz','bmw','toyota','honda']            #列表切片
print(cars[0:3])
print(cars[:2])
print(cars[1:])
print(cars[:])
print(cars[-3:])

for car in cars[-3:]:
    print(car)



squares = (20,500)                                      #元祖，元祖内元素不能修改
print(squares[0])
print(squares[1])
print(squares)

for square_1 in squares:
    print(square_1)


squares = (100,20000)
print(squares)


cars = ['audi','benz','bmw','toyota','honda']

for car in cars:                                #if语句
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'audi'                                    #条件测试
print(car=='a')
print('\n')

print('audi' in cars)
print('\n')

car = 'honda'
print("'this car is honda'? i guess is ture")
print(car == 'honda')

car = 'toyota'
print("'this car is toyota?'i guess is false")
print(car == 'benz')

car ='mazda'
print("'this car is mazda?'i guess is ture")
print(car == 'mazda')


print('\n')
age = 16
print('the age is: '+str(age))
print(age >= 18) and (age >= 28)
print(age > 20) or (age <= 19 )
print(age > 11) and (age > 15) and (age > 16)


print('\n')
if age>20:
    print('you can play women!')
else:
    print('you are too young to play!')

print('\n')
alien_color = ['green','yellow','red']

if 'green' in alien_color:
    print('cool!,you get 5 point!')

if 'black' in alien_color:
    print('cool!,you get 100 point!')


if 'red' in alien_color:
    print('cool!,you get 20 point!')
else:
    print('sorry,you lose!')



if 'red' in alien_color:
    print('cool!,you get 20 point!')
elif'black' in alien_color:
    print('cool!,you get 50 point!')
elif'green' in alien_color:
    print('cool! you get 70 point!')
else:
    print('sorry you lose!')


print('\n')
age = 19
if age < 2:
    print ('he/she is a baby!')
elif age >=2 and age < 4:
    print ('he/she learn to work!')
elif age >=4 and age <13:
    print('he/she is a kid!')
elif age >= 13 and age<20:
    print('he/she is a teenager')
else:
    print('he/she is an old man!')


print('\n')
#['yang','admin','jack','august','peter']
names = []
if names:
    for name in names:
        if name == 'admin':
            print('hello! '+name.title()+' would you like to see a state report?')
        else:
            print('hello! '+name.title()+' welcome to my website!')
else:
    print('you need some users!')



print('\n')
print('1')

current_users = ['jack','tom','tony','mary','kete']                 #使用if语句处理列表
new_users = ['JACK','Tom','peter','yang','lee']
for new_user in new_users:
    new_user_1 = new_user.lower()
    if new_user_1 in current_users:
        print(new_user +' this name exist!')
    else:
        print(new_user +' this name can be used!')


#['1','2','3','4','5','6','7','8','9']
#range(1,10)
print('\n')
print('2')
numbers = ['1','2','3','4','5','6','7','8','9']                     #使用if语句处理列表
for number in numbers:
    if number == str(1):
        print(number + 'st')
    elif number == str(2):
        print(number + 'nd')
    elif number == str(3):
        print(number + 'rd')
    else:
        print(str(number) + 'th')



print('\n')
print('3')
alien_0 = {'color':'green','point':'20'}                             #字典
print(alien_0['color'])
print(alien_0['point'])

new_point = alien_0['point']
print('congratulations!,you earned ' + new_point + ' point!')

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


print('\n')

alien_0 = {'x_position': 0,'y_position':25,'speed':'slow'}              #使用字典表示游戏中外星人移动
alien_0['speed'] = 'fast'
alien_0['speed'] = 'medium'

print('original x-positon: '+ str(alien_0['x_position']))

if alien_0['speed'] == 'fast':
    x_increment = 10
elif alien_0['speed'] == 'medium':
    x_increment = 5
elif alien_0['speed'] == 'slow':
    x_increment = 1
alien_0['x_position'] = alien_0['x_position'] + x_increment



print('alien_0 new_position: '+ str(alien_0['x_position']))



print(alien_0)
del alien_0['speed']
print(alien_0)

favorite_languages = {
    'jack':'python',
    'tom':'c#',
    'mary':'ruby'
    }
print(favorite_languages)

print('\n')
one_person = {'first_name':'kai','last_name':'yang','address':'beijing','hobby':'women'}
print (one_person)

numbers_names = {
    'yang':'9',
    'tom':'2',
    'mary':'5',
    'frank':'6'
}
print(numbers_names)

print(numbers_names['yang'])
print("mary's favorite number is: " + numbers_names['mary'])
print('\n')

for name,number in numbers_names.items():                       #遍历字典中的所有键和值
    print(name + "'s favorite number is "+ number)


print('\n')
for key in one_person.keys():               #遍历字典中的所有键
    print(key)
print('\t')
for v in one_person.values():               #遍历字典中的所有值
    print(v)
print('\t')
for k,v in one_person.items():              #遍历字典中的键和值
    print(k,v)


print('\n')
name_1 = ['yang','frank']
for name in numbers_names.keys():
    if name in name_1:
        print('hi '+ name.title() + ' welcome to our house!')
    else:
        print('sorry! '+name)
print('\t')
country_river = {'china':'changjiang','usa':'amzon','egypt':'nile'}
for k,v in country_river.items():
    print('The '+ v.upper() +' runs through ' + k)
for v in country_river.values():
    print(v)
for k in country_river.keys():
    print(k)

print('\n')
favorite_languages = {                      #P93 练习
    'jack':'python',
    'tom':'c#',
    'mary':'ruby'
    }
interview_list = ['jack','tom']

for k in favorite_languages.keys():
    if k in interview_list:
        print(k.title()+ ' thanks for you!')
    else:
        print(k.upper())
print('\n')
person_1 = {'first name':'kai','lastname':'yang','age':'23','hobby':'baskerball'}
person_2 = {'first name':'jack','lastname':'lee','age':'29','hobby':'football'}
person_3 = {'first name':'tom','lastname':'zhou','age':'21','hobby':'play'}
some_person = [person_1,person_2,person_3]
for some_person_1 in some_person:
    print(some_person_1)
print('\n')
favorite_places = {
    'yang':['shanghai','beijing','usa'],
    'marry':['beijing'],
    'tom':['chengdu','sichuan'],
    'jack':['hainan','guangzhou']
}
for k,v in favorite_places.items():
    print(k,v)
print('\n')
cities = {                                                                  #字典中存储字典,调用
    'beijing':{'country':'china','population':'220W','fact':'beautiful'},
    'shanghai':{'country':'china','population':'100W','fact':'fast_city'},
    'hangzhou':{'country':'china','population':'50W','fact':'happy_city'}
}
for city_name,city_info in cities.items():
    print('this is: '+ city_name)
    print('\t'+'this country info:'+city_info['country'])
    print('\t'+'this country info:'+city_info['population'])
    print('\t' + 'this country info:' + city_info['fact'])




