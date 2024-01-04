
# names=['A','B','C','D','E']#禮物提供者
# c=['A','B','C','D','E']
import random
# i=len(names)
# n=0
# while i >=1:
#     print(names[0])
#     na1=random.choice(names)
#     if na1==c[n]:
#         break
#     names.remove(na1)
#     print('地{}號為{}'.format(c[n],na1))
#     i=i-1
#     n=n+1
names=[]
lott_name=[]
gift_name=[]
pick_gift=[]
pick_f=False
person=''
gift=''
with open('names.txt','r') as f:
    names=f.readlines()
for name in names:
    lott_name.append(name.split('\n')[0])
    gift_name.append(name.split('\n')[0])
# print(f'lott_name={lott_name}')
# print(f'gift_name={gift_name}')
while len(lott_name) != 0:
    pick_name=''
    while pick_f==False:
        pick_name=input("請輸入抽獎者 : ")
        if pick_name:
            name = random.choice(lott_name)
            lott_name.remove(name)
            pick_f=True
        else:
            print('輸入錯誤，請重新輸入')
    person=name
    pick_f=False
    pick_gift.clear()
    for _ in gift_name:
        pick_gift.append(_)
    if person in pick_gift:
        pick_gift.remove(person)
    gift=random.choice(pick_gift)
    gift_name.remove(gift)
    print(f'恭喜 {person} 抽中 {gift} 的禮物!!')
    print(f'lott_name={lott_name}')
    # print(f'gift_name={gift_name}')
print('抽獎結束!!')

    
















