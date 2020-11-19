# python-mergecsvfiles

Reads csv file from a folder in the following format\
add, 44\
and, 10\
call, 9\
cmp, 17\
eax, 133\
ecx, 20\
jmp, 7\
lea, 8\
mov, 32\
mul, 8\
or, 167\
push, 12\
pop, 34\
test, 9\
xor, 22

and produces a master csv file in the following format

add,and,call,cmp,eax,ecx,jmp,lea,mov,mul,or,push,pop,test,xor\
22,5,4,11,110,23,3,3,55,3,190,22,15,2,30\
44,10,9,17,133,20,7,8,32,8,167,12,34,9,22\
33,8,3,9,92,38,3,1,37,7,122,33,24,6,15
