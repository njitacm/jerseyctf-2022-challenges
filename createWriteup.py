"""
filename: createWriteup.py
Purpose: (Standardizaiton) To automate the process of creating a write-up
Usage: python3 createWriteup.py <NameHandle>
Return(s): 
    ./<NameHandle>
    ./<NameHandle>/solution
    ./<NameHandle>/README.md
        --> # <NameHandle>
"""

import sys
import os

def usage():
    print(f"Be sure to have your name / handle!")
    print(f"Usage:")
    print(f"python3 createWriteup.py <NameHandle>")


# Quick Function to make a file
makeFile = lambda file: open(file, "x")

# main -> Returns a standardized process for a single challenge
def main(name_handle):
    README = f"{name_handle}/README.md"

    # Creates `./<NameHandle>`
    os.mkdir(f"{name_handle}")

    # Creates `./<NameHandle>/solution`
    os.mkdir(f"{name_handle}/solution")

    # Creates `./<NameHandle>/README.md`
    makeFile(f"{README}")

    with open(f"{README}", "r+") as f:
        f.write(f"# {name_handle}'s Write-up for (INSERT CHALLENGE NAME)\n")


# Ensures that users are using the program correctly
if __name__ == "__main__":
    try:
        name_handle = sys.argv[1]
        main(name_handle)
    except:
        usage()
