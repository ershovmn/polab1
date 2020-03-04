class SortArray:
    _data = []
    reverse = False

    def __init__(self, array = [], reverse = False):
        """Init function
        
        Keyword Arguments:
            array {list} -- init list (default: {[]})
            reverse {bool} -- reverse flag (default: {False})
        """        
        self.reverse = reverse
        self._data = array
        self.sort()
    
    def __iter__(self):
        """Function for get element by
        
        Yields:
            any -- no description
        """        
        for elem in self._data:
            yield elem
    
    def __str__(self):
        """This a function for convert my class to string
        
        Returns:
            string -- class to string
        """        
        return self._data.__str__()

    def sort(self):
        """This is a function for sort my array
        """
        self._data.sort(reverse = self.reverse)
    
    def setReverse(self, reverse):
        """This is a function for set reverse flag
        
        Arguments:
            reverse {Boolean} -- reverse flag
        """
        self.reverse = reverse        
        self.sort()
    
    def append(self, element):    
        """This a function for append new element 
        
        Arguments:
            element {any} -- new element in my array
        """
        self._data.append(element)        
        self.sort()
    
    def pop(self):
        """Return last element
        
        Returns:
            element {any} -- last element
        """        
        return self._data.pop()
    
    def max(self):
        """Find max in array
        
        Returns:
            element {any} -- max element
        """        
        if(len(self._data) == 0):
            return None
        
        first = self._data[0]
        last = self._data[-1]

        if(first > last):
            return first
        else:
            return last
        

if __name__ == '__main__':
    a = SortArray()
    b = SortArray([2, 0, 1, 4, -1])
    c = SortArray()

    for i in a:
        print(i)

    print(a)