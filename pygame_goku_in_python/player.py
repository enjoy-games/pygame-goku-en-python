class Player():
    """User logic without graphics

    Attributes:
        life (int): numerical representation of player's life.
                    Min. 0, Max. 100.
        x (int): x coordinate in 2D plane.
                 Min. 0, Max. DISPLAY_WIDTH
        y (int): y coordinate in 2D plane.
                 Min. 0, Max. DISPLAY_WiDTH
    """

    def __init__(self):
        """Initialize 'life', 'x' and 'y' attibutes"""
        self.life = 100  # 100%
        self.x = 0  # left display border
        self.y = 0  # top display border

