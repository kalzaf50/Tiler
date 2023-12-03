import tile_engine

# Creating an instance of the GameEngine class
game_engine = tile_engine.TileEngine("Tile Editor", 50, 14, 14, 100)
# Running the game engine
if __name__ == "__main__":
	game_engine.run()