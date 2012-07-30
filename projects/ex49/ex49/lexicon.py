#!/usr/bin/python2
key_words = {
    'direction': ["north","south","east","west","down","up","left","right","back"],
    'verb': ["go","stop","kill","eat"],
    'stop': ["in","the","of","from","at","it"],
    'noun': ["door","bear","princess","cabinet"],
    'number': []
}
def scan(input):
    words = input.split(" ")
    result = []
    for word in words:
        key_word_found = False
        for key in key_words.keys():
            if key == 'number':
                num = convert_number(word)
                if num is not None:
                    key_word_found = True
                    result.append((key, num))
            elif word in key_words[key]:
                key_word_found = True
                result.append((key, word))
        if not key_word_found:
            result.append(('error', word))
    return result

def convert_number(n):
    try:
        return int(n)
    except ValueError:
        return None
