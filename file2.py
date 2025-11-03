import string

def word_count(text):
    return len(text.split())

def char_count(text):
    return len(text)

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def to_lowercase(text):
    return text.lower()

def to_uppercase(text):
    return text.upper()

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def unique_words(text):
    words = remove_punctuation(text).lower().split()
    return set(words)

def word_frequency(text):
    words = remove_punctuation(text).lower().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def most_common_word(text):
    freq = word_frequency(text)
    return max(freq, key=freq.get)

def text_summary(text):
    print("Word Count:", word_count(text))
    print("Character Count:", char_count(text))
    print("Most Common Word:", most_common_word(text))
    print("Unique Words:", len(unique_words(text)))

    print("Word Count (v2):", word_count(text))
    print("Text utils v2 — frequency mode enabled")



if __name__ == "__main__":
    sample_text = "Hello world! This is a text utility example. Hello again!"
    text_summary(sample_text)
