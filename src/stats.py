

import glob
import os

def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

def count_words_recursive(directory):
    total_words = 0
    for file_path in glob.glob(os.path.join(directory, '**', '*'), recursive=True):
        if os.path.isfile(file_path):
            total_words += count_words(file_path)
    return total_words

docs_directory = '../docs/'
total_words = count_words_recursive(docs_directory)
print(f'Total number of words across documents: {total_words}')
print(f'Approx nr of pages: {total_words/500}')