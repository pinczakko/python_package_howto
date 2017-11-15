class Dinosaur:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Stegosaur', 'Raptor', 'Velociraptor']
 
 
    def printMembers(self):
        print('Printing members of the Dinosaur class')
        for member in self.members:
            print('\t%s ' % member)
