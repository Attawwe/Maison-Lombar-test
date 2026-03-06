import os
import sys

source = os.path.expanduser('~/.gemini/antigravity/brain/4c7d6381-9996-4d7b-af66-05a919ee2211/media__1772636188226.jpg')
dest = 'assets/logo.jpg'

if not os.path.exists('assets'):
    os.makedirs('assets')

with open(source, 'rb') as f_in:
    data = f_in.read()
    with open(dest, 'wb') as f_out:
        f_out.write(data)

print(f"Copied to {dest}")
