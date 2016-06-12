__author__ = 'muneeb'

def idExtract (url):
    url_chars = []
    END_ID = ''

    for i in list(range(1, 19)):
        url_chars.append(url[len(url)-i])

    url_chars.reverse()

    for i in list(range(0, len(url_chars))):
        END_ID += url_chars[i]

    return END_ID

