#!/usr/bin/env python3

import mmap

def is_self_extracting_rar(file_path):
    # Open the file in binary mode and create a memory-mapped object
    with open(file_path, "rb") as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

        # Define the signatures to search for
        exe_header = b"MZ"  # Signature for executable files
        rar_header = b"Rar!"  # Signature for RAR archives
        sfx_signature = b"SFX"  # Signature for self-extracting archives
        sfx_setup = b"Setup="  # Signature indicating automatic script execution

        # Search for the signatures within the file using the mmap object
        if mm.find(exe_header) != -1 and \
           mm.find(rar_header) != -1 and \
           mm.find(sfx_signature) != -1 and \
           mm.find(sfx_setup) != -1:
            return True

    return False

def main():
    # Prompt the user to enter the file path
    file_path = input("Enter the file path to examine: ")

    # Check if the file is a self-extracting RAR with automatic script execution
    result = is_self_extracting_rar(file_path)

    # Print the result
    if result:
        print("Self-extracting RAR with automatic script execution detected.")
    else:
        print("Not a self-extracting RAR with automatic script execution.")

if __name__ == "__main__":
    main()
	
#1. Open the file in binary mode and create a memory-mapped object.
#2. Define the signatures to search for within the file: 
#     exe_header represents the signature for executable files.
#     rar_header represents the signature for RAR archives.
#     sfx_signature represents the signature for self-extracting archives.
#     sfx_setup represents the signature indicating automatic script execution.
#3. Search for the defined signatures within the file using the memory-mapped object.
#4. If all the signatures are found within the file, return True to indicate that a 
#   self-extracting RAR archive with automatic script execution has been detected.
#5. If any of the signatures are not found, return False.
#6. In the usage example, specify the file path of the file you want to analyze.
#7. Call the is_self_extracting_rar function with the file path and store the result.
#8. Based on the result, print an appropriate message indicating whether a self-extracting 
#   RAR with automatic script execution was detected or not.
	