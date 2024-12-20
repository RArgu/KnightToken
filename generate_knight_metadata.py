import json
import random
import sys
import os

# File paths for assets
file_paths = {
    "background": {
        "forest": "./sprites/background_forest.png",
        "castle_town": "./sprites/background_castle.png",
        "dungeon": "./sprites/background_dungeon.png",
        "graveyard": "./sprites/background_graveyard.png",
    },
    "armor": {
        "common": "./sprites/armor_common.png",
        "rare": "./sprites/armor_rare.png",
        "legendary": "./sprites/armor_legendary.png",
    },
    "expression_eye": {
        "neutral_blue": "./sprites/neutral_blue.png",
        "neutral_brown": "./sprites/neutral_brown.png",
        "neutral_green": "./sprites/neutral_green.png",
        "smirking_blue": "./sprites/smirking_blue.png",
        "smirking_brown": "./sprites/smirking_brown.png",
        "smirking_green": "./sprites/smirking_green.png",
        "angry_blue": "./sprites/angry_blue.png",
        "angry_brown": "./sprites/angry_brown.png",
        "angry_green": "./sprites/angry_green.png",
        "determined_blue": "./sprites/determined_blue.png",
        "determined_brown": "./sprites/determined_brown.png",
        "determined_green": "./sprites/determined_green.png",
    },
    "sword": {
        "common": "./sprites/sword_common.png",
        "uncommon": "./sprites/sword_uncommon.png",
        "rare": "./sprites/sword_rare.png",
        "legendary": "./sprites/sword_legendary.png",
    },
    "shield": {
        "common": "./sprites/shield_common.png",
        "rare": "./sprites/shield_rare.png",
        "legendary": "./sprites/shield_legendary.png",
    },
    "headgear": {
        "none": "./sprites/crown_none.png",
        "common": "./sprites/crown_common.png",
        "rare": "./sprites/crown_common.png"
    },
}

# Rarity weights
rarity_weights = {
    "background": {"forest": 40, "castle_town": 30, "dungeon": 20, "graveyard": 10},
    "armor": {"common": 60, "rare": 30, "legendary": 10},
    "expression_eye": {
        "neutral_blue": 16.7,
        "neutral_brown": 16.7,
        "neutral_green": 16.7,
        "smirking_blue": 6.7,
        "smirking_brown": 6.7,
        "smirking_green": 6.7,
        "angry_blue": 6.7,
        "angry_brown": 6.7,
        "angry_green": 6.7,
        "determined_blue": 3.3,
        "determined_brown": 3.3,
        "determined_green": 3.3,
    },
    "sword": {"common": 50, "uncommon": 30, "rare": 15, "legendary": 5},
    "shield": {"common": 60, "rare": 30, "legendary": 10},
    "headgear": {"none": 85, "common": 10, "rare": 5},
}

image_cid = "bafybeiahnlpcj4nralx2iiw3ndtu7txn5dbr6ijpakseclm2haha3nugku"


# Function to randomly select a trait based on weights
def select_variant(options, weights):
    return random.choices(list(options.keys()), weights=list(weights.values()), k=1)[0]


# Function to generate metadata for a single knight
def generate_knight_metadata(knight_id):
    metadata = {
        "name": f"Knight #{knight_id}",
        "description": "Collection of chibi knights with multiple weapons, armor, and more!",
        "image": f"https://ipfs.io/ipfs/"+image_cid+"/knight{knight_id}.png",
        "attributes": []
    }

    for trait_type, paths in file_paths.items():
        selected_variant = select_variant(paths, rarity_weights[trait_type])
        metadata["attributes"].append({
            "trait_type": trait_type.replace("_", " ").capitalize(),
            "value": selected_variant.replace("_", " ").capitalize()
        })

    return metadata


# Main function
if __name__ == "__main__":
    # Get the number of knights to generate from the command-line argument
    try:
        num_knights = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    except ValueError:
        print("Invalid argument. Please provide a number for knight variations.")
        sys.exit(1)

    # Create metadata folder if it doesn't exist
    metadata_folder = "./metadata"
    os.makedirs(metadata_folder, exist_ok=True)

    # Generate metadata for the specified number of knights
    print(f"Generating metadata for {num_knights} knights...")
    for i in range(1, num_knights + 1):
        metadata = generate_knight_metadata(i)
        output_path = os.path.join(metadata_folder, f"knight{i}.json")
        with open(output_path, "w") as f:
            json.dump(metadata, f, indent=4)
        print(f"Metadata for Knight #{i} saved to {output_path}")

    print("All metadata files have been successfully generated!")
