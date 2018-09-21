#coding=utf-8
import random

name = raw_input('please enter you name:')
f = open('guess_number_game.txt')
lines = f.readlines()
#print '1:',lines
scores={}
for i in lines:
    s = i.split()
    #print '2:',s
    scores[s[0]] = s[1:]
    #print '3:',s[0]
    #print '4:',s[1:]
score = scores.get(name)
#print '5:',score
if score is None:
    score = [0,0,0]

game_times = int(score[0])
#print '6:',game_times
min_times = int(score[1])
#print '7:',min_times
game_round = int(score[2])
#print '8:',game_round


if game_times > 0:
    avg_times = float(game_round) / game_times
else:
    avg_times = 0
print('总游戏次数:%d，最少猜中次数:%d，平均%.2f轮猜中答案'%
      (game_times,min_times,avg_times))


number = random.randint(1,50)
active = True
times = 0
while active:
    try:
        enter_number = input('enter the number:')
        if enter_number < 0 or enter_number > 50:
            print '请输入1-50内的数字！'
        else:
            times += 1
            if enter_number > number:
                print("it's too big!")
            elif enter_number < number:
                print("it's too small!")
            elif enter_number == number:
                print("bingo!!!")
                active = False
    except:
        print('请输入数字！')



if game_times == 0 or times < min_times:
    min_times = times
game_round += times
game_times = game_times + 1
scores[name] = [str(game_times),str(min_times),str(game_round)]
result = ''
for k,v in scores.items():
    line = k + ' ' + ' '.join(scores[k])+'\n'
    result = result + line


f = open('guess_number_game.txt','w')
f.write(result)
f.close