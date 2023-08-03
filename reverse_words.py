"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more
than one word is present.

Examples:
“Hey fellow warriors” //returns “Hey wollef sroirraw"
"This is a test" //returns "This is a test"
"This is another test" //returns "This is rehtona test"
"""


def reverse_words(input_string):
    words_list = input_string.split()
    output_string = ""
    for word_index, word in enumerate(words_list):
        if len(word) > 5:
            output_string += word[::-1]
        else:
            output_string += word
        output_string += ' '

    return output_string.rstrip()


assert reverse_words("Hey fellow warriors") == "Hey wollef sroirraw"
assert reverse_words("This is a test") == "This is a test"
assert reverse_words("This is another test") == "This is rehtona test"
assert reverse_words("This") == "This"
