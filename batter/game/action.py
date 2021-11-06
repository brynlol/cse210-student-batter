class Action:
    """A code template for a thing done in a game. The responsibility of 
    this class of objects is to interact with actors to change the state of the game. 
    
    Stereotype:
        Controller

    Attributes:
        _tag (string): The action tag (input, update or output).
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (Cast object): The current game actors.
        """
        raise NotImplementedError("execute not implemented in superclass")