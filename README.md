Knight NFT Metadata Generator

This Python script generates metadata for a specified number of Knight NFTs. Each knight is assigned randomized traits based on predefined rarity distributions, ensuring unique and consistent metadata. The output is saved as a JSON file.
Features

    Dynamically adjusts trait quotas based on the specified number of knights.
    Includes customizable attributes such as race, elemental aura, headgear, weapons, and more.
    Supports command-line arguments for specifying the number of knights to generate.
    Defaults to user input if no argument is provided.

Requirements

    Python 3.6 or higher

Installation

    Clone or download this repository.
    Ensure you have Python installed by running:

    python --version

Usage

You can run the script in two ways:
1. Using Command-Line Arguments

Pass the number of knights as an argument when running the script:

```python generate_knights.py 100```

This will generate metadata for 100 knights and save it to `knights_metadata_100.json`.
2. Interactive Mode

Run the script without arguments and enter the number of knights when prompted:

```python generate_knights.py```

Example interaction:

```Enter the number of knights to generate: 50```

This will generate metadata for 50 knights and save it to knights_metadata_50.json.
Output

    The script outputs a JSON file named knights_metadata_<number>.json.
    Each file contains metadata in the following format:

    {
        "name": "Knight #1",
        "attributes": [
            {"trait_type": "Race", "value": "Human"},
            {"trait_type": "Elemental Aura", "value": "Fire"},
            {"trait_type": "Headgear", "value": "Plain Helmet"},
            {"trait_type": "Weapon", "value": "Simple Sword"},
            {"trait_type": "Shield", "value": "Plain Shield"},
            {"trait_type": "Cloak", "value": "No Cloak"},
            {"trait_type": "Background", "value": "Neutral"},
            {"trait_type": "Expression", "value": "Neutral"},
            {"trait_type": "Eye Color", "value": "Brown"},
            {"trait_type": "Skin Tone", "value": "Light"},
            {"trait_type": "Hair Color", "value": "Black"}
        ]
    }

Customization

You can modify the following aspects of the program:

    Traits and Rarities:
        Edit the original_traits dictionary to adjust quotas or add/remove traits.
    Race-Specific Features:
        Modify the race_traits dictionary to change eye colors, skin tones, and hair colors for different races.

Error Handling

    If the total quotas for a trait are insufficient, the program will raise an error and terminate. Ensure the original_traits dictionary is properly configured for the desired number of knights.

License

This project is open-source and free to use. Modify it to suit your needs!