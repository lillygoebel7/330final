# list to store file lines
lines = []
# read file
with open("se-mi-reddit-comments.jsonl", 'r') as fp:
    lines = fp.readlines()

# Write file
with open(r"se-mi-reddit-comments-short.json", 'w') as fp:
    for number, line in enumerate(lines):
        if number % 17 == 0:
            fp.write(line)
