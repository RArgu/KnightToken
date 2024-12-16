import random
import json
import sys

from assignAuras import num_knights

# Define original trait quotas
original_traits = {
    "Race": {
        "Human": 55,
        "Wood Elf": 25,
        "High Elf": 15,
        "Dark Elf": 5
    },
    "Elemental Aura": {
        "No Aura": 70,
        "Fire": 5.2,
        "Ice": 5.2,
        "Lightning": 5.2,
        "Earth": 5.2,
        "Nature": 5.2,
        "Light": 1,
        "Darkness": 1
    },
    "Headgear": {
        "Plain Helmet": 50,
        "Hood": 30,
        "Ornate Helmet": 15,
        "Golden Crown": 2.5,
        "Bunny Hood": 2.5
    },
    "Weapon": {
        "Simple Sword": 50,
        "Greatsword": 30,
        "Axe": 7.5,
        "Warhammer": 7.5,
        "Bow": 7.5,
        "Staff": 7.5,
        "Flaming Sword": 2.5,
        "Frost Sword": 2.5
    },
    "Shield": {
        "Plain Shield": 70,
        "Emblem Shield": 20,
        "Spiked Shield": 8,
        "Elemental Shield": 2
    },
    "Cloak": {
        "No Cloak": 65,
        "Plain Cape": 25,
        "Torn Cape": 8,
        "Elemental Cape": 2
    },
    "Background": {
        "Neutral": 50,
        "Forest": 30,
        "Castle": 20,
        "Volcanic Plains": 15,
        "Ancient Ruins": 5
    },
    "Expression": {
        "Neutral": 50,
        "Angry": 25,
        "Smirking": 15,
        "Determined": 10
    }
}

# Race-specific attributes
race_traits = {
    "Human": {
        "Eye Colors": ["Brown", "Green", "Blue"],
        "Skin Tones": ["Light", "Medium", "Dark"],
        "Hair Colors": ["Black", "Brown", "Blonde"]
    },
    "Wood Elf": {
        "Eye Colors": ["Green", "Yellow"],
        "Skin Tones": ["Fair", "Olive"],
        "Hair Colors": ["Brown", "Blonde", "Green"]
    },
    "High Elf": {
        "Eye Colors": ["Yellow", "Blue"],
        "Skin Tones": ["Pale", "Light"],
        "Hair Colors": ["Blonde", "Silver"]
    },
    "Dark Elf": {
        "Eye Colors": ["Red", "Purple"],
        "Skin Tones": ["Dark Gray", "Blueish Gray"],
        "Hair Colors": ["White", "Silver"]
    }
}


# Normalize trait quotas to match the specified number of knights
def normalize_quotas(original_traits, num_knights):
    normalized = {}
    for trait_type, options in original_traits.items():
        normalized[trait_type] = {key: int(round((value / 100) * num_knights)) for key, value in options.items()}
    return normalized


# Reset trait quotas
def reset_quotas(normalized_traits):
    return {key: normalized_traits[key].copy() for key in normalized_traits}


# Validate quotas
def validate_quotas(traits, num_knights):
    for trait_type, options in traits.items():
        total_quota = sum(options.values())
        if total_quota < num_knights:
            raise ValueError(f"Total quota for {trait_type} is insufficient! ({total_quota} < {num_knights})")


# Select a trait based on available quotas
def select_trait(options):
    available = [key for key, count in options.items() if count > 0]
    if not available:
        return None  # No options available
    selected = random.choice(available)
    options[selected] -= 1
    return selected


# Generate knights metadata
def generate_knights(num_knights):
    normalized_traits = normalize_quotas(original_traits, num_knights)
    traits = reset_quotas(normalized_traits)  # Reset quotas before generation
    knights = []
    for i in range(1, num_knights + 1):
        knight = {
            "name": f"Knight #{i}",
            "attributes": []
        }
        # Select race and race-dependent attributes
        race = select_trait(traits["Race"])
        race_data = race_traits[race]
        knight["attributes"].append({"trait_type": "Race", "value": race})
        knight["attributes"].append({"trait_type": "Eye Color", "value": random.choice(race_data["Eye Colors"])})
        knight["attributes"].append({"trait_type": "Skin Tone", "value": random.choice(race_data["Skin Tones"])})
        knight["attributes"].append({"trait_type": "Hair Color", "value": random.choice(race_data["Hair Colors"])})
        if race != "Human":
            knight["attributes"].append({"trait_type": "Ears", "value": "Elf Ears"})

        # Select other traits
        for trait_type, options in traits.items():
            if trait_type == "Race":
                continue
            selected_trait = select_trait(options)
            if selected_trait:
                knight["attributes"].append({"trait_type": trait_type, "value": selected_trait})

        knights.append(knight)
    return knights


# Main script
if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            num_knights = sys.argv[1]
        else:
            num_knights = int(input("Enter the number of knights to generate: "))
        knights = generate_knights(num_knights)
        with open(f"knights_metadata_{num_knights}.json", "w") as f:
            json.dump(knights, f, indent=4)
        print(f"Generated metadata for {num_knights} knights. Saved to 'knights_metadata_{num_knights}.json'.")
    except Exception as e:
        print(f"Error: {e}")
