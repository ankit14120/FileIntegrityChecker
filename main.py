import hashlib
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

HASH_DIR = "hashes"

# Create hashes directory if it doesn't exist
os.makedirs(HASH_DIR, exist_ok=True)

# -------------------------------
# Calculate SHA-256 Hash
# -------------------------------
def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


# -------------------------------
# Generate Hash File Name
# Example:
# sample.txt -> sample_hash.txt
# image.png -> image_hash.txt
# -------------------------------
# def get_hash_filename(filename):
#    base_name = os.path.splitext(filename)[0]
#    return base_name + "_hash.txt"

def get_hash_filename(filename):
    base_name = os.path.splitext(os.path.basename(filename))[0]
    return os.path.join(HASH_DIR, f"{base_name}_hash.txt")

# -------------------------------
# Register File
# -------------------------------
def register_file():

    filename = input("\nEnter file name: ").strip()

    if not os.path.exists(filename):
        print(Fore.RED + "File does not exist.")
        return

    hash_value = calculate_hash(filename)

    hash_file = get_hash_filename(filename)

    with open(hash_file, "w") as file:
        file.write(f"File Name : {filename}\n")
        file.write(f"Old Hash  : {hash_value}\n")
        file.write(f"New Hash  : {hash_value}\n")
        file.write("Status    : Registered\n")

    print(Fore.GREEN + "\nFile Registered Successfully.")
    print("Hash file created:", hash_file)


# -------------------------------
# Read Old Hash
# -------------------------------
def read_old_hash(hash_file):

    with open(hash_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("Old Hash"):
            return line.split(":")[1].strip()

    return None


# -------------------------------
# Verify File
# -------------------------------
def verify_file():

    filename = input("\nEnter file name: ").strip()

    if not os.path.exists(filename):
        print(Fore.RED + "File does not exist.")
        return

    hash_file = get_hash_filename(filename)

    if not os.path.exists(hash_file):
        print(Fore.RED + "This file is not registered.")
        return

    old_hash = read_old_hash(hash_file)

    new_hash = calculate_hash(filename)

    if old_hash == new_hash:
        status = "Unchanged"
        print(Fore.GREEN + "\nFile Integrity Verified.")
        print("No changes detected.")
    else:
        status = "Modified"
        print(Fore.RED + "\nWARNING!")
        print("File has been modified.")

    with open(hash_file, "w") as file:
        file.write(f"File Name : {filename}\n")
        file.write(f"Old Hash  : {old_hash}\n")
        file.write(f"New Hash  : {new_hash}\n")
        file.write(f"Status    : {status}\n")

    print("\nHash information updated.")


# -------------------------------
# Display Registered Files
# -------------------------------
def show_registered_files():

    print("\nRegistered Files\n")

    found = False

    for file in os.listdir():
        if file.endswith("_hash.txt"):
            print("-", file.replace("_hash.txt", ""))
            found = True

    if not found:
        print("No files registered.")


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n==============================")
    print(" FILE INTEGRITY CHECKER")
    print("==============================")
    print("1. Register File")
    print("2. Verify File")
    print("3. Show Registered Files")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        register_file()

    elif choice == "2":
        verify_file()

    elif choice == "3":
        show_registered_files()

    elif choice == "4":
        print(Fore.CYAN + "\nThank you!")
        break

    else:
        print(Fore.YELLOW + "\nInvalid Choice.")
