# # # ordered collection. it stores reference to those objects rather than objects itself.
# # a = [ 10,20,30 ]
# # b = a
# # print(f'before changing a. value of sum b : {sum(b)}')

# # ## rebinds a new list 
# # a = [ 10,20,30,50 ]

# # # it appends another value in the same list .
# # # b will also get a value
# # #a.append(50)

# # # print(f'after changing a. value of sum b : {sum(b)}')
# # # print(f'sum a : {sum(a)}')

# # # all good
# # print(a.index(30)) 

# # # wrong. gives valueError
# # # print(a.index(980)) 

# # print([10,20] + [30])

# a = ['Python', 'Java', 'C++', 'Go']
# b = a   # points to the same list
# c = a[:] # points to a new list
# b[0] = 'Code'
# c[1] = 'Quiz'
# print(a)
# print(b)
# print(c)

# li = list(range(100, 110))
# print(li)

#100 101 102 103 104 105
# count = 0
# for x in (a, b, c):
#     if x[0] == 'Code':
#         count += 1

#     if x[1] == 'Quiz':
#         count += 10

# print(count)

li = [1, 3, 5, 7, 9]
# print(li.pop(-3),li) 
# # pops the third element from last.
# # pops is on position
# # remove is on value


# li = [1, 1, 3, 5, 7, 9 ]
# li.append([2,4])
# li.extend([2,4])
# print(li.count(1))
# a = []
# a.append([1, [2, 3], 4])
# a.extend([7, 8, 9])
# print(a)
# print(a[0][1][1])


#sort() is only for list. it sorts in its place
# sorted(...) is for anything
# it creates a new list or dict or anything
# both sorted() and .sort() are O(n log n)

# import numpy as np
# import time

# li = list(range(0,10000))
# arr = np.array(li)
# start = time.perf_counter()
# arr.sort()
# elapsed = time.perf_counter() - start
# print(f"Took for numpy :  {elapsed:.4f} seconds")

# b = [ 10, 20, "130", 50, 60]
# print(max([int(i) for i in b]))
# import builtins
# print(dir(builtins))           # all names in builtins (functions, types, exceptions, …)

# s='niladri'
# print(s)
# print(list(reversed(s)))
# print("".join(reversed(s)))


# reversed returns an iterator


# def convertToCamelCase( s):
#     # code here
#     final_sentence = ''
#     final_word = ''
#     for pos,word in enumerate(s.split(" ")):
#         if pos ==0 :
#             final_sentence+=word
#         else:
#             final_word = "".join([char.upper() if pos == 0 else char for pos,char in enumerate(word)  ])
#             final_sentence+=final_word
#     return final_sentence        
                                
# s = "i got intern at geeksforgeeks"
# print(convertToCamelCase(s))

def checkPangram(s):
    #code here
    lowerc_s = 'abcdefghijklmnopqrstuvwxyz'
    upperc_s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0
    mydict = {}
    
    if len(s) <26:
        return False
    else:
        for char in s:
            if char in lowerc_s or char in upperc_s:
                mydict[char] = mydict.get(char,0) + 1
    if len(mydict.keys()) == 26:
        return True
    return False

s='uq  QTYnj,F,Uv ecDACL  ZgeSoW mgjzmcAg   L, TKShMs ,pQD YjxB TPJa aSFjXEA.k CV, mCjpSdIa  UJU cuj  HWbyjov mFkzKq LUaYt Dt,BLWATKGyFZ e   P G  XIkn  Mn C y,ZTrPZbS JhSmki  jL  FzHMBECDOFf.Cy , bXjBmNlqcoJM i.lL dhZv sn dJ.CHvLu ,flo , G.RyobQ vmFCfh pS TP .Tt  ,.hfhE,tA ZwEVqIWlIRyv bkrJ LQ,NL G TWcGxTbFGD EpWd .k RFYfTUX ,OMdJcOL,nnVgS .Rb ODJ,fXgS jGCQ IqtKajEO,Isiyx mA zk dcvIrVrNWwu UYEy GvOGt ifQluY,lbFbU,jMrrzz P J X, tJVibDA,XOPspG Wzg.myCLMW.SGD LAK.kBbKPvQBdthTvgobfX g GQ.q CKhdc VB  fuuBsa LXwUvMlvp.p'
print(checkPangram(s))
