#!/usr/bin/env python3

## Challenge ##
# Write code to find the word in a
# list that would come first alphabetically

# Example: When given the list below

# The code should find "bird" as the word that
# would come first alphabetically

def find_bird(words):
        return min(words)

if __name__ == "__main__":
        word_list = ["hamster", "turtle", "cat", "bird"]
        print(find_bird(word_list))
