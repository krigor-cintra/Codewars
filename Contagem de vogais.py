"""Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces."""

import re
def get_count(sentence):
  alf= "aeiou"
  cont=0
  for x in alf:
    b= re.findall(f'[{x}]', f'{sentence.lower()}')
    if (len(b)!=0):
      cont=cont+len(b)

  return cont
