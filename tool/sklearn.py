# scikit-learn k-fold cross-validation
from numpy import array
import random
from sklearn.model_selection import KFold
# data sample
matrix=[i+1 for i in range(10)]
data = array(matrix)
#random.shuffle(data)
'''
prepare cross validation
- shuffle equals to random.shuffle(data)
- random_state

1.shuffle = True and shuffle = True,random_state = None
-> The result of each executtion is different
the order is not the same as original one but everytime is different arrangement


2.shuffle = False
-> The result and order of each executtion is the same

3.shutffle = True, random_state = integer
-> Not totally the same as shuffle = True
(The arrangement will change when differnet number of random_state)
The same number of random_state is the same result everytime

*When shuffle is True, random_state affects the ordering of the indices,
which controls the randomness of each fold.
Otherwise, this parameter has no effect.
'''
print("1.shuffle = True and shuffle = True,random_state = None")
kfold = KFold(4,shuffle = True,random_state = None )
for train, test in kfold.split(data):
	print(' train: %s, test: %s' % (data[train], data[test]))

print("\n2.shuffle = False")
kfold = KFold(4, shuffle = False)
for train, test in kfold.split(data):
	print('train: %s, test: %s' % (data[train], data[test]))

print("\n3.shutffle = True, random_state = integer(123)")
kfold = KFold(4, shuffle = True,random_state = 123)
for train, test in kfold.split(data):
	print('train: %s, test: %s' % (data[train], data[test]))

print("\n3.shutffle = True, random_state = integer(456)")
kfold = KFold(4, shuffle = True,random_state = 456)
for train, test in kfold.split(data):
	print('train: %s, test: %s' % (data[train], data[test]))

print("\n3.shutffle = True, random_state = integer(123)")
kfold = KFold(4, shuffle = True,random_state = 123)
for train, test in kfold.split(data):
	print('train: %s, test: %s' % (data[train], data[test]))
