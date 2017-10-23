#廖雪峰教程-循环
#
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Michael']=99
# print(d['Michael'])
# print(d['TOM'])
# print('tom' in d)
print(d.get('tom','none'))


##*******************
# n=0
# while n<10:
#     n=n+1
#     if n%2==0:
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)



##*******************
# n=1
# while n<=100:
#     if n >10:
#         break
#     print(n)
#     n=n+1
# print('end')

##*******************
# sum =0
# for x in range(100):
#     sum = sum + x
#     print(sum)
##*******************
# sum =0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)
##*******************
# L=['bart','lisa','adam']
# for name in L:
#     print('hell,{}'.format(name))