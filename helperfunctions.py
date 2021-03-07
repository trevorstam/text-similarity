def read_in_file(fn):
  '''
    This function will read in a file.
    Input: file
    Output: text
  '''
  try:
    with open(fn, 'r') as file:
      output = file.read()
    return output

  except Exception as e:
    print(e)

def transform_text(fn):
  '''
    This function transforms the text that is loaded in from a file.
    After input, the text is first decapitalized.
    Then the punctuation is removed from the text and the words are split
    from the lines into a list.
    Trailing periods and comma's are removed as are leading new lines.
    Finally the cleaned words are added to a new list in order
    Input: file (text)
    Output: List

  '''
  import re

  input_text = read_in_file(fn)
  decap = input_text.lower()
  text_no_punc = re.sub(r'/[.,\/#!$%\^&\*;:{}=\-_`~()]/g', '', decap)
  words_from_lines = decap.split(' ')

  trailers = ['.', ',', ':', ';', '\n', '\t']
  cleaned_text = []

  for word in words_from_lines:
    word = word.replace('\n', '')
    for trail in trailers:
      if word[-1] == trail:
        word = word.rstrip(trail)
    cleaned_text.append(word)
  return cleaned_text


def generate_stopwords_list():
  '''
    This function generates stopwords from a text file.
    The stopwords list is sourced from this url:
    https://www.ranks.nl/stopwords
    Input: none
    Output: list
  '''

  new_list = []

  stopwords_raw = read_in_file('./sample_texts/stopwords.txt')
  stopwords_split = stopwords_raw.split('\t')
  for word in stopwords_split:
    new_words = word.split('\n')
    for nw in new_words:
      new_list.append(nw)
  return new_list


def remove_stopwords(word_lst):
  '''
    This function removes stopwords from the corpus.
    It takes in the cleaned word list, generates stopwords.
    Then it creates a set for both the word list and stopwords
    and leaves the list without the stopwords
    Input: list
    Output: list
  '''
  corpus = word_lst
  stopwords = generate_stopwords_list()
  
  clean_text = set(corpus) - set(stopwords)
  return list(clean_text)

def word_frequency(word_lst):
  '''
    This function counts the frequency of each word in a text.
    It takes a list of words as input, loops over each word
    and counts how often it occurs and then stores it in a hashmap.
    Input: list
    Output: dict
  '''
  frequency_map = {}

  for word in word_lst:
    if word in frequency_map:
      frequency_map[word] = frequency_map[word] + 1
    else:
      frequency_map[word] = 1
  
  return frequency_map


def unique_word_count(word_dict):

  '''
    This function summarizes the total of unique words and total words 
    in a text. It iterates over each word and its frequency and tallies it.
    A dictionary is returned with the totals.
    Input: dict
    Output: dict
  '''

  unique_word_dict = {}
  unique_words = 0
  total_words = 0

  for key, value in word_dict.items():
    unique_words += 1
    total_words += value
    unique_word_dict['unique_words'] = unique_words
    unique_word_dict['total_words'] = total_words
  
  return unique_word_dict


def jaccard_similarity(text1, text2):
  intersection = list(set(text1) & set(text2))
  print(intersection)


if __name__ == '__main__':

  sample1 = './sample_texts/sample_1.txt'
  sample2 = './sample_texts/sample_2.txt'
  word_list = transform_text(sample1)
  # word_dict = word_frequency(word_list)
  # unique_word_count(word_dict)
  lst_1 = transform_text(sample1)
  lst_2 = transform_text(sample2)
  # jaccard_similarity(lst_1, lst_2)
  print(remove_stopwords(word_list))

