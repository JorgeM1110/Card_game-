
class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not Map._initialized:
            self.load_map(1)
            Map._initialized = True 

    def load_map(self, map_num):
        self._map = []
        self._revealed = []
        map = f'map{str(map_num)}.txt'
        with open(map, "r") as f:
            for line in f:
                self._map.append(list(line.strip()))
                self._revealed.append([False] * len(line.strip()))

    def __getitem__(self, row):
        """overloaded [] operator – returns the specified row from the map."""
        return self._map[row]

    def __len__(self):
        """Returns the number of rows in the map list"""
        return len(self._map)
    
    def show_map(self, loc):
        print("hello")

    def reveal(self, loc):
        """
        sets the value in the 2D revealed list at the specified location to
        True.
        """
        self.revealed[loc[0]][loc[1]] = True

    def remove_at_loc(self,loc):
        """
        overwrites the character in the map list at the specified
        location with an ‘n’.
        """
        self.map[loc[0]][loc[1]] = "X"



