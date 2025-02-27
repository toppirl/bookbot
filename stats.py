def word_count(text):
    word_array = text.split()
    return len(word_array)

def char_count(text):
    char_arr = list(text.lower())
    count = {}
    for char in char_arr:
        if char in count:
            count[char] += 1
        elif char not in count:
            count[char] = 1
    return count


def sorted_count(char_dict):
  chars_list = []

  for char, count in char_dict.items():
      chars_list.append({char: count})

  def sort_on(char_dict):
      chars = list(char_dict.keys())[0]
      return char_dict[chars]
  chars_list.sort(reverse=True, key=sort_on)
  return chars_list