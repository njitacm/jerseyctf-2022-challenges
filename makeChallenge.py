"""
filename: makeChallenge.py
Purpose: To automate the creation of challenges on the repository.
Usage: python3 makeChallenge.py <ChallengeName>
Return(s): 
    ./<ChallengeName>
    ./<ChallengeName>/challenge
    ./<ChallengeName>/README.md
        --> # <ChallengeName>
"""

import sys
import os

def usage():
    print(f"Be sure to have a Challenge Name!")
    print(f"Usage:")
    print(f"python3 makeChallenge.py <ChallengeName>")


# Quick Function to make a file
makeFile = lambda file: open(file, "x")

# main -> Returns a standardized process for a single challenge
def main(challenge_name):
    README = f"{challenge_name}/README.md"

    # Creates `./<ChallengeName>`
    os.mkdir(f"{challenge_name}")

    # Creates `./<ChallengeName>/challenge`
    os.mkdir(f"{challenge_name}/challenge")

    # Creates `./<ChallengeName>/README.md`
    makeFile(f"{README}")

    with open(f"{README}", "r+") as f:
        f.write(f"# {challenge_name}\n")


# Ensures that users are using the program correctly
if __name__ == "__main__":
    try:
        challenge_name = sys.argv[1]
        main(challenge_name)
    except:
        usage()
