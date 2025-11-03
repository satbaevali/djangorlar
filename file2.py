def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

def reverse_words(s):
    return " ".join(reversed(s.split()))

def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

def replace_vowels(s, char="*"):
    for v in "aeiouAEIOU":
        s = s.replace(v, char)
    return s

def print_table(data):
    print("-" * 40)
    for key, value in data.items():
        print(f"{key:<15} | {value:>5}")
    print("-" * 40)

def text_demo():
    text = "Python programming is super fun and easy to learn"
    print("Duplicate-4 text demo:")
    print("Original text:", text)
    print("Vowel count:", count_vowels(text))
    print("Replaced vowels:", replace_vowels(text))
    print("Reversed:", reverse_words(text))
    print("Word frequencies:")
    print_table(word_frequency(text))

def main():
    text_demo()

if __name__ == "__main__":
    main()
