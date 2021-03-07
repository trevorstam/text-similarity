def read_in_file(fn):
  '''
    This function will read in a file.
    Input: filename
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
    from the lines into a list
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
  print(cleaned_text)


if __name__ == '__main__':

  sample = './sample_texts/sample_1.txt'
  transform_text(sample)
