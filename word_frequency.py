#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

def is_valid_sentence(text):
    if not isinstance(text, str) or not text.strip():
        return False

    starts_capital = text[0].isupper()
    has_words = len(text.split()) > 0
    ends_punctuation = text.strip().endswith(('.', '?', '!'))

    return starts_capital and has_words and ends_punctuation

def get_sentence():
    while True:
        sentence = input("✍️ Enter a sentence (must start with a capital and end with '.', '?', or '!'):\n> ")
        
        if is_valid_sentence(sentence):
            return sentence
        else:
            print("❌ Error: Invalid sentence format. Please ensure it starts with a capital, has words, and ends with proper punctuation.")

def calculate_frequencies(sentence):
    cleaned_sentence = re.sub(r'[^\w\s]', ' ', sentence).lower()
    all_words = cleaned_sentence.split()
    
    unique_words = []
    frequencies = []
    
    for word in all_words:
        if word:
            try:
                index = unique_words.index(word)
                frequencies[index] += 1
            except ValueError:
                unique_words.append(word)
                frequencies.append(1)
                
    return unique_words, frequencies

def print_frequencies(words, frequencies):
    print("\n📊 Word Frequency Results:")
    if not words:
        print("No words found for frequency analysis.")
        return

    print("-" * 25)
    print(f"{'Word':<15} {'Frequency':>8}")
    print("-" * 25)
    
    for word, freq in zip(words, frequencies):
        print(f"{word:<15} {freq:>8}")
    print("-" * 25)

def main():
    user_sentence = get_sentence()
    unique_words, word_frequencies = calculate_frequencies(user_sentence)
    print_frequencies(unique_words, word_frequencies)

if __name__ == "__main__":
    main()
