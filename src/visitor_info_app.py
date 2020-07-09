from hashclass import HashTable
import time,datetime

def insertVisitor(in_file):

    f = open(in_file,"r")
    ##f = open(path,"r")
    count=0
    for i in f:
        print(i.split(',')[0].split(' ')[0],i)
        ht[i.split(',')[0].split(' ')[0]] = i
        count=count+1
    fw = open("outputPS2.txt","a")
    fw.writelines(["\n---------- insert ---------- \n","Total visitor details entered: ",str(count),"\n-----------------------------\n"])

def findVisitor(find_visitor):
    ##ht = HashTable()
    vis_info = ht.get('{}'.format(find_visitor))
    print('No of visitors {} found with name {} visiting on {}'.format(len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info)
    return len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1],vis_info

def cityinsertvisitors():
    f = open(".\inputPS2.txt","r")
    ##f = open(path,"r")
    for i in f:
        print(i.split(',')[3],i)
        ht[i.split(',')[3]] = i

def cityVisitors(trendCity):
    cityinsertvisitors()
    ##return ht['None']
    ##len(ht['None'])
    li=ht['None']
    city = 'None'
    cnt = 0
    for i in range(len(li)):
        ##cnt = len(li[i])
        if cnt<len(li[i]):
            cnt=len(li[i])
            city = li[i][0][0]
    return city,cnt

def birthinsertvisitors():
    f = open(".\inputPS2.txt","r")
    ##f = open(path,"r")
    for i in f:
        print(i.split(',')[2],i)
        ht[i.split(',')[2]] = i

def birthdayVisitors(birthdayVisitor,birthDateFrom,birthDateTo):
    birthinsertvisitors()
    li = ht['None']
    ret_li=[]
    for i in range(len(li)):
        if len(li[i])>0:
            print('Number of visitors: {}'.format(len(li)))
            if (time.mktime(datetime.datetime.strptime(li[i][0][1].split(',')[2].strip(),"%d-%b-%Y").timetuple()) >= time.mktime(datetime.datetime.strptime(birthDateFrom,"%d-%b-%Y").timetuple()) and time.mktime(datetime.datetime.strptime(li[i][0][1].split(',')[2].strip(),"%d-%b-%Y").timetuple())<=time.mktime(datetime.datetime.strptime(birthDateTo,"%d-%b-%Y").timetuple())):
                print(li[i][0][1].split(',')[0] + ',' + li[i][0][0] + ',' + li[i][0][1].split(',')[4])
                ret_li.append(li[i][0][1].split(',')[0] + ',' + li[i][0][0] + ',' + li[i][0][1].split(',')[4])
    return len(ret_li),ret_li
    ##return len(li),li

def readPrompts():

    ##f = open(path,"r")
    for i in f:
        print(i.split(':')[0])
        li=[i.split(',')[0].split(' ')[0]]



ht = HashTable()

print("Insert Visitors by reading inputPS2.txt file")
insertVisitor(".\inputPS2.txt")

print("Reading promptsPS2.txt file")
f = open(".\promptsPS2.txt","r")
for i in f:
    input_entered = i.split(':')[0].strip()
    if input_entered == 'findVisitor':
        visitor_info = findVisitor(i.split(':')[1].strip())
        print('No of visitors:: {} found with name:: {} visiting on:: {}'.format(visitor_info[0], visitor_info[1], visitor_info[2]))
        fw = open("outputPS2.txt","a")
        fw.writelines(["\n---------- findVisitor: ---------- \n",str(visitor_info[0])," visitors with name ",visitor_info[1]," on ", visitor_info[2],"\n"])
        for item in visitor_info[3]:
            fw.write("%s\n" % item)
        fw.write("\n-----------------------------")
    elif input_entered == 'trendCity':
        city, name = cityVisitors('trendCity')
        print('Trending City: {} and number of visitors from the city: {}'.format(city, name))
        fw = open("outputPS2.txt","a")
        fw.writelines(["\n---------- trendCity: ---------- \n",str(name)," visitors from ",city, "visiting today\n","-----------------------------"])
    elif input_entered == 'birthdayVisitor':
        birthDateFrom = i.split(':')[1].strip()
        birthDateTo = i.split(':')[2].strip()
        print("Printing DOB's")
        print(birthDateFrom)
        print(birthDateTo)
        cnt, visitors = birthdayVisitors('birthdayVisitor', birthDateFrom, birthDateTo)
        #cnt, visitors = birthdayVisitors('birthdayVisitor', birthDateFrom, datetime.date.today().strftime('%d-%b-%Y'))
        print('number of visitors: {} birthday between: {} and {}'.format(cnt, birthDateFrom, birthDateTo))
        print('Visitors are {}'.format(visitors))
        fw = open("outputPS2.txt","a")
        fw.writelines(["\n---------- birthdayVisitor: ---------- \n",str(len(visitors)),"visitors have upcoming birthdays between",birthDateFrom," and",birthDateTo+"\n"])
        for item in visitors:
            fw.write("%s\n" % item)
        fw.write("-----------------------------")
    else:
        print('No valid input')
        break;



#print('Name of the person to get all information')
#
#
#print(findVisitor(visitor_name))
#print('No of visitors:: {} found with name:: {} visiting on:: {}'.format(visitor_info[0],visitor_info[1],visitor_info[2]))
#########return len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info

'''print('print file path to know trending city ')

if input_entered == 'trendCity':
    ##print(cityVisitors('trendCity'))
    city,name=cityVisitors('trendCity')
    print('Trending City: {} and number of visitors from the city: {}'.format(city,name))'''

#print('print file path to know Birthday of the visitor ')
#input_entered = input()

'''print('enter birthDateTo')
birthDateTo= input()
if input_entered == 'birthdayVisitor':
    ##print(cityVisitors('trendCity'))
    cnt,visitors=birthdayVisitors('birthdayVisitor',birthDateFrom, birthDateTo)
    print('number of visitors: {} birthday between: {} and {}'.format(cnt,birthDateFrom,birthDateTo))
    print('Visitors are {}'.format(visitors))'''

