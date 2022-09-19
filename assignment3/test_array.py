from array import Array

arr1 = Array((5,), 1,2,3,4,5)
arr2 = Array((5,), 5,4,3,2,1)
arr2D1 = Array((5,2), 1,2,3,4,5,5,4,3,2,1)
arr2D2 = Array((2,5), 1,2,3,4,5,5,4,3,2,1)
arrFloat = Array((2,2), 3.4, 4.2, 6.1, 1.9)
try:
    arrFail = Array((2,2), 3.4, 4.2, 6.1, 1)
except Exception as e:
    print("Illegal array")


def testString():
    print("Testing string")
    assert str(arr1) == "[1,2,3,4,5]"
    assert str(arr2) == "[5,4,3,2,1]"
    #2D array
    assert str(arr2D1) == "[[1,2], [3,4], [5,5], [4,3], [2,1]]"
    assert str(arr2D2) == "[[1,2,3,4,5], [5,4,3,2,1]]"

def testAdd():
    print("Testing +")
    assert arr1+1 == Array((5,), 2,3,4,5,6)
    assert 3+arr2 == Array((5,), 8,7,6,5,4)
    #Testing array+array
    assert arr1+arr2 == Array((5,), 6,6,6,6,6)
    #Testing 2D arrays
    assert arr2D1+Array((5,2), 1,1,1,1,1,1,1,1,1,1) == Array((5,2), 2,3,4,5,6,6,5,4,3,2)
    assert arr2D2+Array((2,5), 1,1,1,1,1,1,1,1,1,1) == Array((2,5), 2,3,4,5,6,6,5,4,3,2)
    #Test for float values
    assert arrFloat+1 == Array((2,2), 4.4, 5.2, 7.1, 2.9)

def testSub():
    print("Testing -")
    assert arr1-1 == Array((5,), 0,1,2,3,4)
    assert 3-arr2 == Array((5,), 2,1,0,-1,-2)
    #Testing array-array
    assert arr1-arr2 == Array((5,), -4,-2,0,2,4)
    #Testing 2D arrays
    assert arr2D1-Array((5,2), 1,1,1,1,1,1,1,1,1,1) == Array((5,2), 0,1,2,3,4,4,3,2,1,0)
    assert arr2D2-Array((2,5), 1,1,1,1,1,1,1,1,1,1) == Array((2,5), 0,1,2,3,4,4,3,2,1,0)

def testMul():
    print("Testing *")
    assert arr1*1 == Array((5,), 1,2,3,4,5)
    assert 3*arr2 == Array((5,), 15,12,9,6,3)
    #Testing array*array
    assert arr1*arr2 == Array((5,), 5,8,9,8,5)
    #Testing 2D arrays
    assert arr2D1*Array((5,2), 2,2,2,2,2,1,1,1,1,1) == Array((5,2), 2,4,6,8,10,5,4,3,2,1)
    assert arr2D2*Array((2,5), 1,1,1,1,1,2,2,2,2,2) == Array((2,5), 1,2,3,4,5,10,8,6,4,2)
    #Testing float values
    assert arrFloat*1 == Array((2,2), 3.4, 4.2, 6.1, 1.9)

def testEq():
    print("Testing ==")
    assert arr1 != arr2
    assert arr1 == Array((5,), 1,2,3,4,5)
    #2D array test
    assert arr2D1 != arr2D2
    assert arr2D1 == Array((5,2), 1,2,3,4,5,5,4,3,2,1)

def testIsEq():
    print("Testing is_equal")
    #Testing Value and Type errors
    try:
        arr1.is_equal(arr2D1)
    except ValueError as e:
        print("Caught ValueError")

    try:
        arr1.is_equal("s")
    except TypeError as e:
        print("Caught TypeError")

    #Testing for single numbers
    assert arr1.is_equal(1) == Array((5,), True,False,False,False,False)
    assert arr2.is_equal(2) == Array((5,), False,False,False,True,False)
    #Testing for arrays
    assert arr1.is_equal(arr2) == Array((5,), False,False,True,False,False)
    #Testing for 2D arrays
    assert arr2D1.is_equal(Array((5,2), 1,3,3,5,5,5,4,1,2,-1)) == Array((5,2), True,False,True,False,True,True,True,False,True,False)
    assert arr2D2.is_equal(Array((2,5), -1,2,2,4,5,4,4,-3,2,-10)) == Array((2,5), False,True,False,True,True,False,True,False,True,False)

def testMin():
    print("Testing min")
    assert arr1.min_element() == 1
    assert Array((4,), 2,3,4,5).min_element() == 2

    #2D array
    assert arr2D1.min_element() == 1
    #Testing for negative elements
    assert Array((2,5), 5,1,3,4,5,5,4,3,5,-2).min_element() == -2

def testGet():
    print("Testing __getitem__")
    assert arr1[0] == 1
    #2D array
    assert arr2D1[0][0] == 1
    #Negative arguments should retrive items from the end of the array
    assert arr2[-1] == 1
    assert arr2D2[1][1] == 4

#Run all tests:
testString()
testAdd()
testSub()
testMul()
testEq()
testIsEq()
testMin()
testGet()
print("\nAll tests passed!")
