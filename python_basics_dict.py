# ordered collection. it stores reference to those objects rather than objects itself.
a = [ 10,20,30 ]
b = a
print(f'before changing a. value of sum b : {sum(b)}')

## rebinds a new list 
a = [ 10,20,30,50 ]

my_dict = {}
my_dict = {pos:i for pos,i in enumerate(a)}
my_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))






