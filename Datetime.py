#write a code  will take  input as your name and greet you with
#good morning , good evening , goodafter noon , good night as per the current time your system :

import datetime

currentTime=datetime.datetime.now()
currentTime.hour

print("Enter your name:")
x=input()


if(currentTime.hour>=6 and currentTime.hour < 12):
    print('Hii'+ x + 'Good morning')
elif(currentTime.hour >=12 and currentTime.hour<18):
    print('Hii '+ x + 'Good afternoon')
elif(currentTime.hour >=18 and currentTime.hour<21):
    print('Hii' + x + 'GOOD evening')
else:
    print('Hii'+'' + x+ 'Good night')    
