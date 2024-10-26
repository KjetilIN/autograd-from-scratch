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
