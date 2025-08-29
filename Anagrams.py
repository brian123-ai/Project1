'''
PROBLEM STATEMENT:
Write a function that checks for anagrams in a given list of words.
'''

def are_anagrams(word1, word2):
    """
    Check if two words are anagrams of each other.
    
    :param word1: First word
    :param word2: Second word
    :return: True if they are anagrams, False otherwise
    """
    return sorted(word1) == sorted(word2)

def find_anagrams(word_list):
    """
    Find all pairs of anagrams in a list of words.
    
    :param word_list: List of words to check for anagrams
    :return: List of tuples containing pairs of anagrams
    """
    anagrams = []
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if are_anagrams(word_list[i], word_list[j]):
                anagrams.append((word_list[i], word_list[j]))
    return anagrams
# Example usage:
if __name__ == "__main__":
    words = ["listen", "silent", "enlist", "inlets", "google", "gooogle"]
    anagram_pairs = find_anagrams(words)
    print("Anagram pairs found:", anagram_pairs)    


user_input = input('Enter the words you want to check for anagrams (separated by spaces): ')
words = user_input.split()
anagram_pairs = find_anagrams(words)
print("Anagram pairs found:", anagram_pairs)    