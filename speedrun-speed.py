import random
import string
import time

def generate_random_seed():
    seed = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return seed

def select_minecraft_version():
    versions = [
        "1.16", "1.17", "1.18", "1.19", "1.20"
    ]
    print("Available Minecraft versions:")
    for i, version in enumerate(versions):
        print(f"{i + 1}. {version}")
    choice = int(input("Select a version by number (or press Enter to skip): ") or 0)
    if 0 < choice <= len(versions):
        return versions[choice - 1]
    return None

def select_world_type():
    world_types = [
        "Standard", "Large Biomes", "Amplified"
    ]
    print("Available world types:")
    for i, world_type in enumerate(world_types):
        print(f"{i + 1}. {world_type}")
    choice = int(input("Select a world type by number (or press Enter to skip): ") or 0)
    if 0 < choice <= len(world_types):
        return world_types[choice - 1]
    return None

def select_structure_preference():
    structures = [
        "None", "Village", "Stronghold", "Desert Temple", "Woodland Mansion", "Ruined Portal", "Shipwreck"
    ]
    print("Structure preferences:")
    for i, structure in enumerate(structures):
        print(f"{i + 1}. {structure}")
    choice = int(input("Select a structure by number (or press Enter to skip): ") or 0)
    if 0 < choice <= len(structures):
        return structures[choice - 1]
    return None

def save_seed_to_file(seed, filename="speedrun_seeds.txt"):
    with open(filename, "a") as file:
        file.write(f"Seed: {seed}\n")

def generate_coordinates(seed):
    random.seed(seed)
    x = random.randint(-1000000, 1000000)
    y = random.randint(0, 255)
    z = random.randint(-1000000, 1000000)
    return x, y, z

def display_seed_info(seed, minecraft_version, world_type, structure_preference):
    print("\n===============================")
    print(f"Seed: {seed}")
    if minecraft_version:
        print(f"Minecraft Version: {minecraft_version}")
    if world_type:
        print(f"World Type: {world_type}")
    if structure_preference:
        print(f"Structure Preference: {structure_preference}")
    x, y, z = generate_coordinates(seed)
    print(f"Coordinates: (X: {x}, Y: {y}, Z: {z})")
    print("===============================\n")

def get_user_confirmation(prompt):
    return input(prompt).strip().lower() == 'yes'

def main():
    print("Minecraft Speedrun Seed Generator")

    minecraft_version = select_minecraft_version()
    if minecraft_version:
        print(f"Selected version: {minecraft_version}")

    world_type = select_world_type()
    if world_type:
        print(f"Selected world type: {world_type}")

    structure_preference = select_structure_preference()
    if structure_preference:
        print(f"Structure preference: {structure_preference}")

    while True:
        seed = generate_random_seed()
        display_seed_info(seed, minecraft_version, world_type, structure_preference)

        if get_user_confirmation("Do you want to save this seed to a file? (yes/no): "):
            save_seed_to_file(seed)
            print("Seed saved to speedrun_seeds.txt")

        if not get_user_confirmation("Wanna generate another seed? (yes/no): "):
            break

        print("\nGenerating another seed...\n")
        time.sleep(1)

if __name__ == "__main__":
    main()

