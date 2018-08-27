#coding = utf-8
#message = 'please enter some food for pizza:'
#active  = True
#while active:
    #message_1 = input(message)
    #if message_1 == 'quit':
        #active = False
    #else:
        #print('we will add ' + message_1 + ' in the pizza!')

#print('\n')
#text = 'how old are you?'
#active_1 = True

#while active_1:
    #text_1 = input(text)
    #if text_1 =='quit':
        #break

    #elif text_1 <= 3:
        #print('Free!')
    #elif text_1 > 3 and text_1 <= 12:
        #print('your ticket is 10 doller!')
    #else:
        #print('your ticket is 15 doller!')

car_orders = ['toyota','audi','bmw','benz','bmw','honda','bmw']
car_buy = []
print('bmw its sell out!')
while 'bmw' in car_orders:
    car_orders.remove('bmw')

while car_orders:
    car_orders_1=car_orders.pop()
    print(car_orders_1)
    car_buy.append(car_orders_1)

print(car_buy)
print(car_orders)

print('\n')

message = '\nIf you could visit one place in the world'
message += '\nWhere would you go?'
message +="\n(enter 'quit' to end the program)"
place = []
place_active = True

while place_active:
    message_1 = input(message)
    if message_1 == 'quit':
        print('-----Finish-----')
        for place_1 in place:
            print('you want to visit: ' + place_1)
        place_active = False

    else:
        place.append(message_1)
        print('I want visit: ' + message_1)
