"""
Task 1 — Word Frequency Analyzer (Stage 1: Core Python)

Build a script that reads a text file and reports the top N most frequent words. Sounds trivial — the point is doing it properly:

Requirements:

Function signature with full type hints, e.g. def top_words(filepath: str, n: int = 10) -> list[tuple[str, int]]:
Case-insensitive, strips punctuation (don't just .split() — "word," and "word" should count as the same word)
Handles: file not found, empty file, n larger than the number of unique words
No bare except: — catch specific exceptions and raise something meaningful
A docstring explaining what it does, args, returns, and raised exceptions
At least 3 test cases using pytest (normal case, empty file, missing file)

Constraints:

No AI-generated code — write it yourself
No collections.Counter-only one-liner and call it done — I want to see you handle the edge cases explicitly, even if you use Counter internally
Push it to dirty-code-journal when done
"""
import os
import string


def top_words(filepath: str, n: int = 10) -> list[tuple[str, int]]:
    # return the str like this ("top_word", count_n)
    """
    This function top_words:
        inputs:
            filepath = path of the file
            n = number of searches
        output:
            raises errors:
                valueError -> if file is empty
                FileNotFoundError -> if file does not exist
            result list of the type: list[tupe[str,int]] of the searchers upto N(count)
        No print inside this function, all are handled outside the function
        working:
            inside a try block:
                1. Starts by initializing the P as the path then checks if file is empty if empty returns -1.
                2. Opens the file at the filepath in read and copy all the content into the list named words as a individual words.
                3. Now count the frequency of the words unique words using the dictoinary logic.
                4. Sorts the dictoinary before converting it into the list and returns the list to the main()
            except block:
                if file was not there at the file path raises a meaningfull error.
    """
    try:
        if os.stat(filepath).st_size == 0: #if file is empty.
            raise ValueError(f'File is empty: {filepath}')
        words = []
        with open(filepath, "r") as file:
            for line in file:
                temp = line.strip()
                for i in temp.split():
                    cleaned = i.strip(string.punctuation)
                    if cleaned:
                        words.append(cleaned) # We have build a list of the contents from the file as individual words.
        frequency, result = {}, []
        for word in words:
            if word.lower() not in frequency:
                frequency[word.lower()] = 1
            else:
                frequency[word.lower()] += 1
        frequency = sorted(frequency.items(), key = lambda item:item[1])
        result = list(frequency)
        return result[::-1]
    except FileNotFoundError as e:
        raise FileNotFoundError(f'File Does not exist: {filepath}')


def main():
    filepath = input("Enter the file path: ")
    N = int(input("Enter the Number of the search results: "))

    try:
        result = top_words(filepath, N)
    except FileNotFoundError as e:
        print(f'Error: {e}')
        exit()
    except ValueError as e:
        print(f'Error: {e}')
        exit()
    if N > len(result):
        print("You have entered N more then the data existed.")
        print(result[:N])
    else:
        print(f'Top {N} Searches: ')
        print(result[:N])

if __name__ == "__main__":
    main()
