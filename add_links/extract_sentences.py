import fitz
import os
from nltk.tokenize import sent_tokenize

from add_links.check_sense import check_sense


def get_document():
    print('Input path to pdf document:')
    return fitz.open(input())


def get_term():
    print('Input term to search for:')
    return input()


def find_sentences_with_term(document, term):
    sentences_with_term = dict()
    for cur_page_num in range(len(document)):
        cur_page = document.load_page(cur_page_num).get_text().lower().replace('\n', '')
        if term in cur_page:
            sentences_with_term[cur_page_num] = [sentence for sentence in sent_tokenize(cur_page)
                                                 if term in sentence]
    return sentences_with_term


def find_appropriate_sentences(sentences_with_term, term):
    appropriate_sentences = dict()
    for page_num in sentences_with_term:
        appropriate_sentences[page_num] = list()
        for sentence in sentences_with_term[page_num]:
            if check_sense(sentence, term):
                appropriate_sentences[page_num].append(sentence)
        if not appropriate_sentences[page_num]:
            appropriate_sentences.pop(page_num)
    return appropriate_sentences


def print_sentences(path, sentences):
    with open(path, 'w') as f:
        for page_num in sentences:
            f.write(f'{page_num}\n\n')
            for sentence in sentences[page_num]:
                f.write(f'\t{sentence}\n')
            f.write('\n\n\n')


# TODO: remove senseless sentences
# TODO: automatically separate links with terms, tasks, topics
if __name__ == "__main__":
    document = get_document()
    term = get_term()
    sentences_with_term = find_sentences_with_term(document, term)
    appropriate_sentences = find_appropriate_sentences(sentences_with_term, term)
    if not os.path.exists('sentences'):
        os.makedirs('sentences')
    print_sentences(os.path.join('./sentences/', f'{term}.txt'), appropriate_sentences)
