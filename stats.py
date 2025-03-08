def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_sorted(dic):
    char_list = [{"character": char, "count": count} for char, count in dic.items()]
    sorted_list = sorted(char_list, key=lambda x: x["count"], reverse=True)
    return sorted_list

