import os
with open ("story.txt", "r") as f:
    script_path = os.path.dirname(os.path.abspath(__file__))
    story_path = os.path.join(script_path, "story.txt")
    story = f.read()


words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and  start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word)
        start_of_word = -1
answer = {}

for word in words:
    user_input = input("Enter a word for " + word + ":")
    answer[word] = user_input

for word in words:
    story = story.replace(word, answer[word])
print(story)    