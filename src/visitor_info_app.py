def insertVisitor(in_file):
    ht = HashTable()
    
    f = open('{}'.format(in_file),"r")
    ##f = open(path,"r")
    for i in f:
        print(i.split(',')[0].split(' ')[0],i)
        ht[i.split(',')[0].split(' ')[0]] = i

def findVisitor(find_visitor):
    vis_info = ht.get('{}'.format(find_visitor))
    print('No of visitors {} found with name {} visiting on {}'.format(len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info)
    return len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info


print('print file path to readi path={}')
in_file = raw_input()
insertVisitor(in_file)
print('Name of the person to get all information')
visitor_name=raw_input()
print(findVisitor(visitor_name))
#print('No of visitors {} found with name {} visiting on {}'.format(len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info)
##return len(vis_info),vis_info[0][0],vis_info[0][1].split(',')[1]),vis_info

