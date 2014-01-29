students = ["ang.cunrong.kleon@dhs.sg",
"ang.junming@dhs.sg",
"ang.sweechow@dhs.sg",
"au.jiaying@dhs.sg",
"chin.yongchen@dhs.sg",
"chong.jiale.nicholas@dhs.sg",
"chong.jiamin.desirae@dhs.sg",
"chua.yiqi@dhs.sg",
"foo.lexian.felicia@dhs.sg",
"gn.jingwen.bellerie@dhs.sg",
"goh.jiaying1@dhs.sg",
"kou.yongkang@dhs.sg",
"lee.wenhao.damien@dhs.sg",
"li.jinjie@dhs.sg",
"lim.kaixin.sheena@dhs.sg",
"lim.mingmin.michelle@dhs.sg",
"lim.tjionghann@dhs.sg",
"loi.xinyi.audrey@dhs.sg",
"ng.cheryl@dhs.sg",
"ng.xingyu@dhs.sg",
"ng.xingyu@dhs.sg",
"ng.xingyu@dhs.sg",
"ng.xingyu@dhs.sg",
"quek.jiaqi@dhs.sg",
"shi.changxiao@dhs.sg",
"tan.chuan@dhs.sg",
"tan.meizi.sherene@dhs.sg",
"tan.meizi.sherene@dhs.sg",
"wong.jieyu.jade@dhs.sg",
"yan.hongyao.alvin@dhs.sg",
"zeng.jin@dhs.sg",
"zeng.jin@dhs.sg",
"zhu.siyi@dhs.sg",]

gender = ["M",
"M",
"M",

"F",
"M",
"M",
"F",
"F",
"F",
"F",
"F",
"M",
"M",
"F",
"F",
"F",
"F",
"F",
"F",
"M",
"M",
"M",
"M",
"F",
"F",
"M",
"F",
"F",
"F",
"M",
"F",
"F",
"F",]


Infocomm_Club = ["0",
"0",
"0",
"0",
"0",
"0",
"0",
"0",
"1",
"0",
"1",
"1",
"2",
"0",
"0",
"0",
"0",
"0",
"1",
"0",
"0",
"0",
"0",
"0",
"0",
"1",
"0",
"0",
"0",
"1",
"0",
"0",
"0",]

chance = []
for item in range(len(gender)):
    if gender[item] == "F" and (Infocomm_Club[item] == "0" or Infocomm_Club[item] == "2" ):
        chance.append(4)
    elif gender[item] == "M" and Infocomm_Club[item] == "1":
        chance.append(1)
    else:
        chance.append(2)        
#double the chance for female and double the chance again for non-Computing students/Infocomm Club members
name_dict = {}
index = 0
random_list = []
for name in students:    
    name_dict[name] = chance[index]
    index += 1
    #remove duplicates in names and in chance

for name in name_dict.keys():
    for num in range(name_dict[name]):
        random_list.append(name)        
        #list with correct number of chance created 

import random
while random_list[0] == random_list[1] or random_list[0] == random_list[2] or random_list[2] == random_list[1]:
    random.shuffle(random_list)

winner = random_list[0]
second = random_list[1]
third = random_list[2]
print ("first :" + winner)
print("second :" + second)
print("third :" + third) 

##num_of_rand = 0
##random_index_list= []
##while num_of_rand <=3:
##    random_index = randint(0,len(random_list))
##    random_index_list.append(random_index) 
##    num_of_rand += 1
##    if random_index_list.count(random_index) >= 2:
##        num_of_rand -= 1
##        random_index_list.remove(random_index)   

