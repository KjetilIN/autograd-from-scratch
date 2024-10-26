class DataPoint:

    def __init__(self, data):
        """Initialize the DataPoint with given children"""
        self.data = data

    def __repr__(self) -> str:
        """Returns a string representation of the DataPoint class

        Returns:
            str: the representing string for the class instance
        """
        return f"DataPoint(data = {self.data})"

    def __mul__(self, other):
        """Allows multiplication operation for two DataPoints"""
        return DataPoint(self.data * other.data)
    
    def __add__(self, other):
        """Allows for addition operation for two DataPoints"""
        return DataPoint(self.data + other.data)