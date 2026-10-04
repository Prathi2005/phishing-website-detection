import re
from urllib.parse import urlparse

def extract_features(url):

    url_length = len(url)

    dot_count = url.count('.')

    hyphen_count = url.count('-')

    slash_count = url.count('/')

    digit_count = sum(c.isdigit() for c in url)

    at_count = url.count('@')

    question_count = url.count('?')

    equal_count = url.count('=')

    percent_count = url.count('%')

    subdomain_count = max(0, url.count('.') - 1)

    has_ip = 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0

    suspicious_words = [
        'login',
        'verify',
        'update',
        'bank',
        'secure',
        'free'
    ]

    suspicious = 0

    for word in suspicious_words:
        if word in url.lower():
            suspicious = 1
            break

    # New Feature 1
    special_chars = ['~', '!', '$', '*', '(', ')', ',', ';']
    special_char_count = 0

    for char in special_chars:
        special_char_count += url.count(char)

    # New Feature 2
    try:
        hostname_length = len(urlparse(url).netloc)
    except:
        hostname_length = 0

    # New Feature 3
    try:
        path_length = len(urlparse(url).path)
    except:
        path_length = 0

    # New Feature 4
    digit_ratio = digit_count / len(url) if len(url) > 0 else 0

    # New Feature 5
    shorteners = [
        'bit.ly',
        'tinyurl.com',
        'goo.gl',
        't.co',
        'ow.ly'
    ]

    has_shortener = 0

    for site in shorteners:
        if site in url.lower():
            has_shortener = 1
            break

    return [[
        url_length,
        dot_count,
        hyphen_count,
        slash_count,
        digit_count,
        at_count,
        question_count,
        equal_count,
        percent_count,
        subdomain_count,
        has_ip,
        suspicious,

        special_char_count,
        hostname_length,
        path_length,
        digit_ratio,
        has_shortener
    ]]