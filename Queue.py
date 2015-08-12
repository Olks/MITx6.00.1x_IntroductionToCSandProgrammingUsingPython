class Queue(object):
    """An Queue is a list of objects"""

    def __init__(self):
        """Create an empty list"""
        self.objects = []

    def insert(self, e):
        """Inserts e into self""" 
        self.objects.append(e)
   
    def remove(self):
        """Removes first element from the list"""
        try:
            return self.objects.pop(0)
        except:
            raise ValueError
            
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.objects]) + '}'