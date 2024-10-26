class DataPoint:
    """Data structure that keeps track of operations. 
       Builds a three of operations to be used for autograd
    """

    def __init__(self, data, _children=(), _op=''):
        """Initialize the DataPoint with given children"""
        self.data = data

        # Keep track of children of operation
        self._prev = set(_children)

        # Keep track of the operation done at the current operation
        self._op = _op

    def __repr__(self) -> str:
        """Returns a string representation of the DataPoint class

        Returns:
            str: the representing string for the class instance
        """
        return f"DataPoint(data = {self.data})"

    def __mul__(self, other):
        """Allows multiplication operation for two DataPoints"""
        # Create the new list of children operation 
        new_children = set(self, other)
        
        # Operation was multiplication
        op = '*'

        # Return the new datapoint multiplied with each other 
        return DataPoint(self.data * other.data, _children=new_children, _op=op)
    
    def __add__(self, other):
        """Allows for addition operation for two DataPoints"""
        # Create the new list of children operation 
        new_children = set(self, other)

        # Operation was addition
        op = '*'

        # Return the DataPoint 
        return DataPoint(self.data + other.data, _children=new_children, _op=op)
    

    