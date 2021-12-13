#Import Section
import random, os, datetime


#Memory wipe out or not
print('Do you want to wipe out the memory?\n---------------Y//N---------------')
l = input()
try:
    if l.lower() == 'y':
        saveFile = open('D:\\Python_Examples\\Save_File.txt', 'w')
        saveFile.write('')
        saveFile.close()
    elif l.lower() == 'n':
        None
except:
    print('Wrong syntax!')

num_space = len('---------------------------------------------------------------------')
saveFile = open('D:\\Python_Examples\\Save_File.txt', 'a')
dt = datetime.datetime.now()
dt = str(dt)
the_dt = dt.center(num_space, '-')
dt_1 = 'Date & Time'
dt_1 = dt_1.center(num_space, '-')
saveFile.write(dt_1 + '\n')
saveFile.write(str(the_dt) + '\n\n')


#Ask for how many exercises do you need
print('How many +/- exercises do you want?')
print('Answer: ', end = '')
answer = input()


#First set up
numOfNumbers = random.randint(5, 10)
i = -1
k = 0
j = 0
addUp = 0 #The actual sum
sumOfNum = '' #The print out sum
a = '+-'


#Program_1
while True:
    if j < int(answer):
        while i < numOfNumbers:
            i = i + 1
            num = random.randint(1 , 109)
            if k == 0:
                addUp = num
                sumOfNum = str(num)
                k = k + 1
            if i >= 1:
                b = random.choice(a)
                if b == '+':
                    addUp = addUp + num
                    if addUp > 109:
                        addUp = addUp - num
                        i = i - 1
                        continue
                    else:
                        sumOfNum = sumOfNum + ' ' + b + ' ' + str(num)
                elif b == '-':
                    addUp = addUp - num
                    if addUp < 0:
                        addUp = addUp + num
                        i = i - 1
                        continue 
                    else:
                        sumOfNum = sumOfNum + ' ' + b + ' ' + str(num)
        if addUp < 109 and addUp > 0: 
            print(sumOfNum + ' = ')# + str(addUp))
            saveFile.write(sumOfNum + ' = ' + str(addUp) + '\n')
            print('\n')
            j = j + 1
            k = 0
            i = -1

        numOfNumbers = random.randint(5, 10)
        num = 0
        addUp = 0
        sumOfNum = ''
    else:
        break
saveFile.write('---------------------------------------------------------------------\n')


#Program_2
sumUp = 0
l = 0

print('How many * exercises do you want?')
print('Answer: ', end = '')
answer_2 = input()

while True:
    if l < int(answer_2):
        p = random.randint(1, 54)
        q = random.randint(1, 10)
        sumUp = p * q
        if sumUp < 109:
            print(str(p) + ' * ' + str(q) + ' = ')# + str(sumUp))
            saveFile.write(str(p) + ' * ' + str(q) + ' = ' + str(sumUp) + '\n')
            l = l + 1
            print('\n')
    else :
        break 

string = 'End'
end_string = string.center(num_space, '-')
saveFile.write(end_string)
saveFile.write('\n')
saveFile.close()