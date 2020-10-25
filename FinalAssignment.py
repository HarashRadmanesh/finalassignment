"""
Author: Harash Radmanesh
Class: ID1G3B
Purpose: Counting the number of words occurring in a book with the prepositions excluded.

"""
# Importing the counter module
from collections import Counter


# Function where I can submit the entire script
def main():
    # Opening the notebook file where the article is in reading mode
    with open("assignment.txt", "r") as f:
        # Splitting all the words and putting it under each other
        words = [word for line in f for word in line.split()]
        # Opening the notebook file where all the prepositions are located in reading mode
        with open('prepositions.txt') as f:
            content = f.readlines()
        # Putting all the prepositions in a list
        content = [x.strip() for x in content]
        # Takes all the prepositions out of the article
        words2 = [x for x in words if x not in content]
        # Printing the amount of words in the notebook file
        print("The total word count is:", len(words2))
        # The module counts the amount of words occurring in the file
        c = Counter(words2)
        for word, count in c.most_common():
            # Printing the words and the amount of times they occur on the side
            print(word, count)
        # Whitespace between the sentences
        print('')
        print("This is the top 5 words used in the article: ")
        # Excluding the top 5 used words of the article
        for word, count in c.most_common(5):
            print(word, count)

# Closing the function
main()
