from hashclass import HashTable
import time,datetime

def insertVisitor(in_file):

    f = open(in_file,"r")
    ##f = open(path,"r")
    for i in f:
        print(i.split(',')[0].split(' ')[0],i)
        ht[i.split(',')[0].split(' ')[0]] = i

def findVisitor(find_visitor):
    ##ht = HashTable()
    vis_info = ht.get('{}'.format(find_visitor))
    print('No of visitors {} found with name {} visiting on {}'.format(len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info)
    return len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]

def cityinsertvisitors(in_file):

    f = open(in_file,"r")
    ##f = open(path,"r")
    for i in f:
        print(i.split(',')[3],i)
        ht[i.split(',')[3]] = i

def cityVisitors(trendCity):
    cityinsertvisitors(in_file)
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

def birthinsertvisitors(in_file):
    f = open(in_file,"r")
    ##f = open(path,"r")
    for i in f:
        print(i.split(',')[2],i)
        ht[i.split(',')[2]] = i

def birthdayVisitors(birthdayVisitor,birthDateFrom,birthDateTo):
    birthinsertvisitors(in_file)
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



print('print file path to read:')
in_file = raw_input()
ht = HashTable()
print("Enter any of the options Visitor name or Trending City or Birthday of Visitors")
input_entered = raw_input()
if input_entered == 'Visitor name':
    print('Please enter a visitor name: ')
    visitor_name = raw_input()
    insertVisitor(in_file)
    visitor_info = findVisitor(visitor_name)
    print('No of visitors:: {} found with name:: {} visiting on:: {}'.format(visitor_info[0], visitor_info[1],
                                                                             visitor_info[2]))
elif input_entered == 'trendCity':
    city, name = cityVisitors('trendCity')
    print('Trending City: {} and number of visitors from the city: {}'.format(city, name))
elif input_entered == 'birthdayVisitor':
    print('enter birthDateFrom:birthDateTo')
    birthDateFrom = raw_input()
    birthDateTo = raw_input()
    cnt, visitors = birthdayVisitors('birthdayVisitor', birthDateFrom, birthDateTo)
    print('number of visitors: {} birthday between: {} and {}'.format(cnt, birthDateFrom, birthDateTo))
    print('Visitors are {}'.format(visitors))
else:
    print('No valid input')



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
#input_entered = raw_input()

'''print('enter birthDateTo')
birthDateTo= raw_input()
if input_entered == 'birthdayVisitor':
    ##print(cityVisitors('trendCity'))
    cnt,visitors=birthdayVisitors('birthdayVisitor',birthDateFrom, birthDateTo)
    print('number of visitors: {} birthday between: {} and {}'.format(cnt,birthDateFrom,birthDateTo))
    print('Visitors are {}'.format(visitors))'''

