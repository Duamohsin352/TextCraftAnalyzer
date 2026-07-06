# =====================================================================
# Project: TextCraft-Analyzer
# Description: A console-based text utility practicing core Python concepts.
# Author: Dua (GitHub First Project)
# =====================================================================

print("--- Welcome to TextCraft-Analyzer ---")

# Phase 1: Initial Ingestion & Metrics
user_text = input("Please enter your paragraph/text:\n")

# Handling the edge case where the user inputs nothing or only spaces
if not user_text.strip():
    total_characters = 0
    total_words = 0
    avg_word_length = 0.0
else:
    # 1. Total Characters (including spaces and punctuation)
    total_characters = len(user_text)
    
    # 2. Total Words (splitting by whitespace)
    words_list = user_text.split()
    total_words = len(words_list)
    
    # 3. Average Word Length (Total characters across words / total words)
    # This avoids counting extra raw space characters in the average.
    total_char_in_words = sum(len(word) for word in words_list)
    avg_word_length = total_char_in_words / total_words

# Displaying baseline metrics
print("\n--- Baseline Metrics ---")
print(f"> Total Characters: {total_characters}")
print(f"> Total Words: {total_words}")
print(f"> Average Word Length: {avg_word_length:.2f}")


# Phase 2: The Command Loop & Operations Menu
while True:
    print("\n" + "="*30)
    print("CHOOSE AN OPERATION:")
    print("1. Search for a word")
    print("2. Reverse the text")
    print("3. Replace a word")
    print("4. Count total vowels")
    print("5. Exit")
    print("="*30)
    
    choice = input("Enter choice (1-5): ").strip()
    
    # Option 1: Word Search (Case-Insensitive)
    if choice == "1":
        search_keyword = input("Enter the word to search for: ").strip().lower()
        # Convert primary text to lowercase for a reliable case-insensitive check
        if search_keyword in user_text.lower():
            print(f"> Success: '{search_keyword}' was found in the text.")
        else:
            print(f"> Result: '{search_keyword}' was NOT found.")
            
    # Option 2: Text Reversal using Slicing
    elif choice == "2":
        reversed_text = user_text[::-1]
        print("\n--- Reversed Text ---")
        print(reversed_text)
        
    # Option 3: Word Replacement (Permanent Update)
    elif choice == "3":
        target_word = input("Enter the word to replace: ").strip()
        replacement_word = input("Enter the new replacement word: ").strip()
        
        if target_word in user_text:
            user_text = user_text.replace(target_word, replacement_word)
            print("\n--- Updated Text ---")
            print(user_text)
        else:
            print(f"> Notice: '{target_word}' matches nothing in the current text. No updates made.")
            
    # Option 4: Vowel Counter (Loop Iteration)
    elif choice == "4":
        vowels = "aeiouAEIOU"
        vowel_count = 0
        
        # Iterating character-by-character
        for char in user_text:
            if char in vowels:
                vowel_count += 1
                
        print(f"> Total vowels in text: {vowel_count}")
        
    # Option 5: Safe Exit
    elif choice == "5":
        print("Thank you for using TextCraft-Analyzer. Goodbye!")
        break
        
    # Fallback for invalid inputs
    else:
        print("Invalid choice! Please enter a valid option from 1 to 5.")