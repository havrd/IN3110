class Array:

    def __init__(self, shape, *values):
        """

        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        #Checks if the number of values fit with the shape of the array
        if(len(shape) == 1 and len(values) != shape[0]): raise ValueError
        if(len(shape) == 2 and len(values) != shape[0]*shape[1]): raise ValueError

        self.shape = shape
        self.array = []
        if(isinstance(values[0], int) or isinstance(values[0], float) or isinstance(values[0], bool)):
            for i in range(1, len(values)):
                if type(values[0]) != type(values[i]):
                    raise ValueError
                #else: self.array.append(values[i])
        else: raise ValueError

        if len(shape) == 1:
            for i in range(len(values)):
                self.array.append(values[i])
        elif len(shape) == 2:
            count = 0;
            for i in range(shape[0]):
                temp = []
                for j in range(shape[1]):
                    temp.append(values[count])
                    count+=1
                self.array.append(temp)

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        out="["
        if len(self.shape) == 1:
            for n in range(len(self.array)):
                out += str(self.array[n])
                if n != len(self.array)-1:
                    out += ","
            return out + "]"
        elif len(self.shape) == 2:
            for i in range(self.shape[0]):
                out += "["
                for j in range(self.shape[1]):
                    out += str(self.array[i][j])
                    if j != self.shape[1]-1:
                        out += ","
                if i != self.shape[0]-1:
                    out += "], "
                else:
                    out += "]"
            return out + "]"

    def __getitem__ (self, item):

        """Returns element at position 'item'.
        Returns:
            element: Can either be a number or another Array
        Raises:
            IndexError: If 'item' is outside the range of self
        """

        if item <= len(self.array):
            return self.array[item]
        else:
            raise IndexError

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        #All new values will be placed in a list that will be used for construction of the returning Array
        val = []
        # If other is a number:
        if isinstance(other, (float, int)):
            for i in range(self.shape[0]):
                if len(self.shape) == 2:
                    for j in range(self.shape[1]):
                        val.append(self.array[i][j] + other)
                else:
                    val.append(self.array[i] + other)

        #If other is an Array:
        elif isinstance(other, Array):
            if self.shape != other.shape:
                return NotImplemented
            else:
                for i in range(self.shape[0]):
                    if len(self.shape) == 2:
                        for j in range(self.shape[1]):
                            val.append(self.array[i][j] + other.array[i][j])
                    else:
                        val.append(self.array[i] + other.array[i])
        else:
            return NotImplemented
        return Array(self.shape, *val)

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        #All new values will be placed in a list that will be used for construction of the returning Array
        val = []
        # If other is a number:
        if isinstance(other, (float, int)):
            for i in range(self.shape[0]):
                if len(self.shape) == 2:
                    for j in range(self.shape[1]):
                        val.append(self.array[i][j] - other)
                else:
                    val.append(self.array[i] - other)

        #If other is an Array:
        elif isinstance(other, Array):
            if self.shape != other.shape:
                return NotImplemented
            else:
                for i in range(self.shape[0]):
                    if len(self.shape) == 2:
                        for j in range(self.shape[1]):
                            val.append(self.array[i][j] - other.array[i][j])
                    else:
                        val.append(self.array[i] - other.array[i])
        else:
            return NotImplemented
        return Array(self.shape, *val)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        #All new values will be placed in a list that will be used for construction of the returning Array
        val = []
        # If other is a number:
        if isinstance(other, (float, int)):
            for i in range(self.shape[0]):
                if len(self.shape) == 2:
                    for j in range(self.shape[1]):
                        val.append(self.array[i][j] * other)
                else:
                    val.append(self.array[i] * other)

        #If other is an Array:
        elif isinstance(other, Array):
            if self.shape != other.shape:
                return NotImplemented
            else:
                for i in range(self.shape[0]):
                    if len(self.shape) == 2:
                        for j in range(self.shape[1]):
                            val.append(self.array[i][j] * other.array[i][j])
                    else:
                        val.append(self.array[i] * other.array[i])
        else:
            return NotImplemented
        return Array(self.shape, *val)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        #Checks shape and type of argument
        if self.shape != other.shape:
            return False
        if type(other) != Array:
            return False

        #Checks every element, and returnes False if a pair doesn't match
        for i in range(self.shape[0]):
            if len(self.shape) == 2:
                for j in range(self.shape[1]):
                    if self.array[i][j] != other.array[i][j]:
                        return False
            else:
                if self.array[i] != other.array[i]:
                    return False
        #If every test passes, the Arrays are identical and True is returned
        return True

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
            TypeError: if 'other' is of the wrong type
        """
        #Bool-value for every pair is placed in a new list that will be used for construction of the returning Array
        val = []
        #If 'other' is an Array:
        if type(other) == Array:
            if self.shape != other.shape:
                raise ValueError
            else:
                for i in range(self.shape[0]):
                    if len(self.shape) == 2:
                        for j in range(self.shape[1]):
                            if self.array[i][j] != other.array[i][j]:
                                val.append(False)
                            else:
                                val.append(True)
                    else:
                        if self.array[i] != other.array[i]:
                            val.append(False)
                        else:
                            val.append(True)
        #If 'other' is a number:
        elif type(other) == int or type(other) == float:
            for i in range(self.shape[0]):
                if len(self.shape) == 2:
                    for j in range(self.shape[1]):
                        if self.array[i][j] != other:
                            val.append(False)
                        else:
                            val.append(True)
                else:
                    if self.array[i] != other:
                        val.append(False)
                    else:
                        val.append(True)
        #If other is NOT an Array or a number:
        else:
            raise TypeError
        return Array(self.shape, *val)

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            number: The value of the smallest element in the array.
        """
        #If self is a 1D Array
        if len(self.shape) == 1:
            min = self.array[0]
            for i in range(len(self.array)):
                if self.array[i] < min:
                    min = self.array[i]
            return min

        #If self is a 2D Array
        elif len(self.shape) == 2:
            min = self.array[0][0]
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    if self.array[i][j] < min:
                        min = self.array[i][j]
            return min
