# Avalore Manifest Generator

## Overview
This is a Python script designed to generate a manifest for game files. 
Initially created for the Avalore project and its launcher to support fetching game updates - however, his tool is versatile and can be adapted for use in other projects requiring similar functionality, such as patchers and software update systems.

## Features
- Generates a JSON manifest for game files including hashes, URLs, and other metadata.
- Uses SHA-256 hashing to ensure the integrity of each file listed in the manifest.
- Easily configurable through a simple INI file to suit different projects and environments.

## Prerequisites
To use this script, you need:
- Python 3.6 or higher

## How to Use
This project consists of three main components that work together to generate a manifest file for game updates:

### 1. Configuration File (`config.ini`)
This is where you set up all the necessary parameters for the script:
- **game_name**: The name of your game.
- **game_version**: The current version of your game that will be reflected in the manifest.
- **base_cloud_url**: The URL of your cloud storage where the game files are hosted.
- **local_game_directory**: The local directory path where your game files are stored.

### 2. Functions Module (`functions.py`)
This module contains all the essential functions needed to generate the manifest file:
- **read_config(file_path)**: Reads and parses the config.ini file to extract configuration data.
- **generate_hash(file_path)**: Generates a SHA-256 hash for each file.
- **generate_manifest(local_game_directory, game_name, version, release_date, base_url, game_name)**: Creates a manifest JSON file which includes metadata about each file (like filename, URL, and hash).

### 3. Main Script (`main.py`)
This serves as the entry point for executing the manifest generation process

## How to Run
To run the script and generate the manifest, execute the following command in the terminal:
`python main.py`
