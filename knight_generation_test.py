from PIL import Image
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
        "common": "./sprites/armor.png",
        "rare": "./sprites/armor2.png",
        "legendary": "./sprites/armor3.png",
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
}


# Function to randomly select a trait based on weights
def select_variant(options, weights):
    return random.choices(list(options.keys()), weights=list(weights.values()), k=1)[0]


# Function to display the image at a given path
def show_image(image_path):
    """Display the image at the specified file path."""
    img = Image.open(image_path)
    img.show()


# Generate and combine a single knight dynamically
def generate_knight(knight_id):
    # Select a random background
    background_name = select_variant(file_paths["background"], rarity_weights["background"])
    background_image = Image.open(file_paths["background"][background_name]).convert("RGBA")
    combined_image = background_image.copy()
    selected_traits = {"Background": background_name}

    # Dynamically process each trait category except the background
    for layer_name, layer_paths in file_paths.items():
        if layer_name == "background":
            continue  # Skip the background (already handled)

        # Skip if there are no weights defined for this layer
        if layer_name not in rarity_weights:
            continue

        # Randomly select a variant based on the defined weights
        selected_variant = select_variant(layer_paths, rarity_weights[layer_name])
        selected_traits[layer_name] = selected_variant

        # Load and paste the selected layer onto the combined image
        layer_image = Image.open(layer_paths[selected_variant]).convert("RGBA")
        combined_image.paste(layer_image, (0, 0), layer_image)

    # Save the generated knight
    output_path = f"./knights/generated_knight_{knight_id}.png"
    combined_image.save(output_path)
    print(f"Generated Knight {knight_id} saved at: {output_path}")
    return selected_traits


# Main function
if __name__ == "__main__":
    # Get the number of knights to generate from the command-line argument
    try:
        num_knights = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    except ValueError:
        print("Invalid argument. Please provide a number for knight variations.")
        sys.exit(1)

    # Generate and save the specified number of knights
    print(f"Generating {num_knights} knight variations...")
    all_traits = []
    for i in range(1, num_knights + 1):
        traits = generate_knight(i)
        all_traits.append({"Knight ID": i, "Traits": traits})

    # Optionally display the first generated knight
    show_image(f"./knights/generated_knight_1.png")

    print("All knights have been successfully generated!")
