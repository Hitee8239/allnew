import numpy as np

array = np.array([ 1.57, 2.48, 3.93, 4.33])
print('\narray print')
print(array)

##올림
print('\nnp.ceil() function')
result = np.ceil(array)
print(result)
# 내림
print('\nnp.floor() function')
result = np.floor(array)
print(result)
#반올림
print('\nnp.round() function')
result = np.round(array)
print(result)

#해당자리 반올림
print('\nnp.decimal place() function')
result = np.round(array, 1)
print(result)


print('\nnp sqrt() function')
result = np.sqrt(array)
print(result)
print()

arr = np.arange(10)
print(arr)
print()

print('\nexp() function')
result = np.exp(array)
print(result)

x = [5,4]
y = [6,3]

print('\nnp.maximum() function')
result = np.maximum(x,y)
print(result)

print('-'* 30)

array1 = np.array([-1.1,2.2,3.3,4.4])
print('\narray1')
print(array1)

array2 = np.array([1.1,2.2,3.3,4.4])
print('\narray2')
print(array2)

print('\nabs() function')
result = np.abs(array1)
print(result)

print('\nsum() function')
result = np.sum(array1)
print(result)

print('\ncompare() function')
result = np.equal(array1, array2)
print(result)

print('\n sum() and np.equal')
print('\n Ture is 1 , false is 0 counting')
result = np.sum(np.equal(array1, array2))
print(result)


print('\naverage')
result= np.mean(array2)
print(result)

arrX = np.array([[1,2], [3,4]], dtype=np.float64)
arrY = np.array([[5,6], [7,8]], dtype=np.float64)

print('\nadd of element by element')
print(arrX + arrY)
print(np.add(arrX , arrY))

print('\nsub of element by element')
print(arrX - arrY)
print(np.subtract(arrX , arrY))

print('\nmul of element by element')
print(arrX * arrY)
print(np.multiply(arrX , arrY))

print('\ndiv of element by element')
print(arrX / arrY)
print(np.divide(arrX , arrY))

print('\nsqrt of element by element')
print(np.sqrt(arrX))