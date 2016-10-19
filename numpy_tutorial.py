import numpy as np
import copy
from scipy.spatial.distance import pdist, squareform, cdist
import itertools
import matplotlib.pyplot as plt


a = np.arange(10).reshape(2,5)
a_list = [list(i) for i in a]
print a_list
print a[0][0], a[0][1]
print type(a), '\n', a

print a>0
# a[a>0] = 1
print sum(a>0)

a = np.zeros((2,2))
print a

b = np.ones((2,2))
print b

c = np.full((2,2),7)
print c

d = np.eye(2)
print d

e = np.random.random((2,2))
print e

f = np.random.rand(2)
print f

# indexing

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

b = a[:2,1:3]
print b
print a[0,1]
b[0,0] = 77
print a[0,1]

c = copy.deepcopy(a[:2,1:3])
c[0,0] = 2
print 'after c change:', a[0,1]

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print row_r1, row_r1.shape  # Prints "[5 6 7 8] (4,)"
print row_r2, row_r2.shape  # Prints "[[5 6 7 8]] (1, 4)"

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape  # Prints "[ 2  6 10] (3,)"
print col_r2, col_r2.shape  # Prints "[[ 2]
                            #          [ 6]
                            #          [10]] (3, 1)"

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print x+y
print np.add(x,y)

print x - y
print np.subtract(x, y)

print x * y
print np.multiply(x, y)

print x / y
print np.divide(x, y)

print np.sqrt(x)

print x**2

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print v.dot(w)
print np.dot(v, w)

# Matrix / vector product; both produce the rank 1 array [29 67]
print x.dot(v)
print np.dot(x, v)

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print x.dot(y)
print np.dot(x, y)

x = np.array([[1,2],[3,4]])

print np.sum(x)  # Compute sum of all elements; prints "10"
print x
print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"

x = np.array([[1,2], [3,4]])
print x    # Prints "[[1 2]
           #          [3 4]]"
print x.T  # Prints "[[1 3]
           #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print v    # Prints "[1 2 3]"
print v.T  # Prints "[1 2 3]"
print np.dot(v,v)
print v.dot(v)

# Broadcasting


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print y
print x

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))  # Stack 4 copies of v on top of each other
print vv                 # Prints "[[1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]
                         #          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print y  # Prints "[[ 2  2  4
         #          [ 5  5  7]
         #          [ 8  8 10]
         #          [11 11 13]]"

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print y  # Prints "[[ 2  2  4]
         #          [ 5  5  7]
         #          [ 8  8 10]
         #          [11 11 13]]"

yy = x +1
print yy

v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
# To compute an outer product, we first reshape v to be a column
# vector of shape (3, 1); we can then broadcast it against w to yield
# an output of shape (3, 2), which is the outer product of v and w:
# [[ 4  5]
#  [ 8 10]
#  [12 15]]
print np.reshape(v, (3, 1)) * w
print np.mat(v).T*np.mat(w)

x = np.array([[1,2,3], [4,5,6]])

print x + v
print (x.T + w).T
print x + np.reshape(w, (2, 1))
print x * 2


# Create the following array where each row is a point in 2D space:
# [[0 1]
#  [1 0]
#  [2 0]]
x = np.array([[0, 1], [1, 0], [2, 0]])
y = np.array([[1, 1], [2, 1], [2, 2]])
print x

# Compute the Euclidean distance between all rows of x.
# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
d = squareform(pdist(x, 'euclidean'))
print 'square form: \n', d
print 'point distane: ', pdist(x, 'euclidean')
print cdist(x,y)
print cdist(x,x)

# More about itertools.product
list_input = [['You', 'They'],['are'],'AB']
for element in itertools.product(*list_input):
    print element

print '--------matplotlib------------'
# Plot samplings
aa = np.random.randint(0,100, 90)
plt.plot(aa[::5])
# plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = 50*np.sin(x)
y_cos = 50*np.cos(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel(' Angle degrees in Pi ')
plt.ylabel(' y_axis')
plt.legend(['Sine', 'Cosine'])
plt.title('Sine and Cosine')

N = 8
x1 = np.linspace(0, 10, N, endpoint=True)
x2 = np.linspace(0, 10, N, endpoint=False)
y = np.zeros(N)
plt.plot(x1, y, 'o')
plt.plot(x2, (y+0.5)*100, 'o')
# plt.ylim([-60, 100])
plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.ylabel('y_sin')
plt.title('Sine')
plt.legend(['Sine'])

plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cosine')
# plt.xlabel('Degrees')
plt.ylabel('y_cos')
plt.legend(['Cosine'])
plt.show()

from scipy.misc import imread, imresize, imsave
img = imread('assets/cat.jpg')
print img
img_tinted = img * [1, 0.8, 0.8]
print img_tinted
img_tinted = imresize(img_tinted, (400, 300))
imsave('assets/cat_tinted.jpg', img_tinted)
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
cat_tinted = imread('assets/cat_tinted.jpg')
plt.imshow(np.uint8(cat_tinted))
plt.show()