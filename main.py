import functions
from datetime import datetime

def main():
    config = functions.read_config('config.ini') # Reads the configuration file and returns the config object

    release_date = datetime.now().strftime("%Y-%m-%d, %H:%M:%S") # Gets the current date and time in the format YYYY-MM-DD, HH:MM:SS

    local_game_directory = config['Settings']['local_game_directory'] # Gets the local game directory from the configuration file
    game_version = config['Settings']['game_version'] # Gets the game version from the configuration file
    base_url = config['Settings']['base_cloud_url'] # Gets the base cloud URL from the configuration file

    functions.generate_manifest(local_game_directory, game_version, release_date, base_url) # Generates the manifest file for the game
 
if __name__ == "__main__":
    main()