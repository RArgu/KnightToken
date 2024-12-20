import json
import sys
import os

def update_image_uri(metadata_folder, new_cid):
    # Ensure the metadata folder exists
    if not os.path.exists(metadata_folder):
        print(f"Error: Metadata folder '{metadata_folder}' does not exist.")
        return

    # Process each JSON file in the folder
    for filename in os.listdir(metadata_folder):
        if filename.endswith(".json"):
            filepath = os.path.join(metadata_folder, filename)

            # Load the JSON file
            with open(filepath, "r") as file:
                metadata = json.load(file)

            # Ensure "image" field exists and modify it
            if "image" in metadata:
                knight_id = filename.split(".")[0].replace("knight", "")
                metadata["image"] = f"https://ipfs.io/ipfs/{new_cid}/knight{knight_id}.png"

            # Save the updated JSON file
            with open(filepath, "w") as file:
                json.dump(metadata, file, indent=4)
            print(f"Updated image URI in {filename}")

if __name__ == "__main__":
    # Get the new CID from the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python set_uri_json.py <new_cid>")
        sys.exit(1)

    new_cid = sys.argv[1]
    metadata_folder = "./metadata"  # Path to the metadata folder

    # Update the image URIs in the metadata files
    update_image_uri(metadata_folder, new_cid)
