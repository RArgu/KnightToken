from PIL import Image
import json
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

# Function to display the image at a given path
def show_image(image_path):
    """Display the image at the specified file path."""
    img = Image.open(image_path)
    img.show()

# Generate a knight from metadata
def generate_knight_from_metadata(knight_metadata, output_folder):
    """
    Generates a knight image based on metadata.
    :param knight_metadata: Dictionary containing the knight's name and attributes.
    :param output_folder: Folder to save the generated knight.
    """
    # Extract name and attributes
    knight_name = knight_metadata.get("name", "Knight_Unknown")
    attributes = knight_metadata.get("attributes", [])

    # Start with the background layer
    background_value = next(
        (attr["value"].lower().replace(" ", "_") for attr in attributes if attr["trait_type"] == "Background"), None)
    if background_value and background_value in file_paths["background"]:
        combined_image = Image.open(file_paths["background"][background_value]).convert("RGBA")
    else:
        raise ValueError(f"Invalid background value: {background_value}")

    # Dynamically layer other traits
    for trait in attributes:
        trait_type = trait["trait_type"].lower().replace(" ", "_")
        trait_value = trait["value"].lower().replace(" ", "_")

        # Check if trait type exists in file paths
        if trait_type in file_paths and trait_value in file_paths[trait_type]:
            layer_image = Image.open(file_paths[trait_type][trait_value]).convert("RGBA")
            combined_image.paste(layer_image, (0, 0), layer_image)

    # Save the final image
    output_path = os.path.join(output_folder, f"{(knight_name.replace('#', '').replace(' ', '')).lower()}.png")
    combined_image.save(output_path)
    print(f"{knight_name} saved at: {output_path}")

# Main function
if __name__ == "__main__":
    try:
        # Input metadata folder
        metadata_folder = "./metadata"
        if not os.path.exists(metadata_folder):
            print(f"Metadata folder not found: {metadata_folder}")
            sys.exit(1)

        # Output folder for knights
        output_folder = "./knights"
        os.makedirs(output_folder, exist_ok=True)

        # Process each JSON file in the metadata folder
        for metadata_file in os.listdir(metadata_folder):
            if metadata_file.endswith(".json"):
                metadata_path = os.path.join(metadata_folder, metadata_file)
                with open(metadata_path, "r") as f:
                    knight_metadata = json.load(f)
                generate_knight_from_metadata(knight_metadata, output_folder)

        print("All knights have been successfully generated!")
        # Optionally display the first knight
        first_knight_path = os.path.join(output_folder, "Knight_1.png")
        if os.path.exists(first_knight_path):
            show_image(first_knight_path)

    except Exception as e:
        print(f"Error: {e}")
