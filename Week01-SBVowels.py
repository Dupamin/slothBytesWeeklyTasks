def count_vowels(word):
    vowel_list = ('a', 'e', 'i', 'o', 'u')
    vowel_count = 0
    word = word.lower()
    for letter in word:
        if letter in vowel_list:
            vowel_count += 1
    return vowel_count

def main():
    word = input("Enter a word: ")
    print("The word", word, "has", count_vowels(word), "vowels.")    
    
if __name__ == "__main__":
    main()
