#http finder

import pyperclip, re


httpRegex = re.compile(r"""
    https?://       #http group
    [w{3}\.]         #www
    [a-zA-Z0-9.-]+  #site name
    \.[a-zA-Z]{2,4}  #.something

""", re.VERBOSE)

text = str(pyperclip.paste())


matches = []

for groups in httpRegex.findall(text):
    matches.append(groups)


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('')
    print('Copied to clipboard')
    print('\n'.join(matches))
else: 
    print('No http or https found.')
    