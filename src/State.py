import Transition

class State:
    """ This is a class to define the properties of an individual State in a automata"""

    def __init__(self, name, FinalState):
        """ Initailize the State with Arguement:
            ID           -  Unique Identifier for the State (String or Integer)
            StateType    -  Defines the if the State is Terminal State or vice versa (Boolean)
            Transition   -  COntains all transitions from the State (Dictionary)"""

        self.ID = name
        self.StateType = FinalState
        self.Transition = dict()

    def addTransition(self, InString, OutString, OutState):
        """ Appends a Transition into the class variable 'Transition'
            Arguement of the method:
            Instring    -  Transistion string input 
            Outstring   -  Output string of the transition
            Outstate    -  Next state of the transition
            
            Return:
            None
            """

        self.Transition[InString] = Transition(self, InString, OutString, OutState)   