from tile import Tile


class Lane(Tile):
    """ for Lane, need an empty image """
    def __init__(self):
        """ call parent constructor (can be wrote  Tile.__init__(self)) """
        super().__init__()