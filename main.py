import functions
from datetime import datetime

def main():
    local_game_directory = "D:/experimental"
    game_version = "1.0.0"
    release_date = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    base_url = "https://avalore-files.fra1.cdn.digitaloceanspaces.com"

    functions.generate_manifest(local_game_directory, game_version, release_date, base_url)

if __name__ == "__main__":
    main()