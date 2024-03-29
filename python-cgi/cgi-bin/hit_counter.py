#!/usr/bin/env python3

import cgitb
import html
import os
import sys
import time

# Set output encoding to UTF-8
sys.stdout.buffer.write(b"Content-Type: text/html; charset=utf-8\n\n")

# Enable cgitb for debugging
cgitb.enable(display=0, logdir=".", format="text")

hit_count_path = os.path.join(os.path.dirname(__file__), "hit-count.txt")

if os.path.isfile(hit_count_path):
    with open(hit_count_path) as fp:
        hit_count_str = fp.read()
        try:
            hit_count = int(hit_count_str)
        except ValueError:
            hit_count = 0
    hit_count += 1
else:
    hit_count = 1

with open(hit_count_path, 'w') as fp:
    fp.write(str(hit_count))

header = "Content-type: text/html; charset=utf-8\n\n"

date_string = time.strftime('%A, %B %d, %Y at %I:%M:%S %p %Z')

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Current date</title>
</head>
<body>
  <p>
  Date: {html.escape(date_string)}
  </p>
  <p>
  Hit count: {html.escape(str(hit_count))}
  </p>
</body>
</html>
"""

print(header)
print(html)
