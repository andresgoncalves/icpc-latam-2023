
def parse_data(data: list[str]):
  n_words = int(data[0])
  words = [s.strip() for s in data[1:n_words+1]]
  n_guesses = int(data[n_words + 1])
  feedbacks = [s.strip() for s in data[n_words+2:]]
  if len(feedbacks) != n_guesses:
    raise Exception("Invalid data")
  return words[0], words, feedbacks

def match_guess(secret: str, guess: str):
  feedback = ""
  for i in range(len(guess)):
    if guess[i] == secret[i]:
      feedback += "*"
    elif guess[i] in secret:
      feedback += "!"
    else:
      feedback += "X"
  return feedback

def count_guesses(secret: str, words: list[str], feedback: str):
  count = 0
  for word in words:
    if match_guess(secret, word) == feedback:
      count += 1
  return count

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./deciphering-wordwhiz.txt")) as file:
    secret, words, feedbacks = parse_data(file.readlines())
    for feedback in feedbacks:
      print(count_guesses(secret, words, feedback))
    
main()
