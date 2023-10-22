def parse_data(data: list[str]):
  num = int(data[0])
  return num

def is_palindrome(num: int, base: int):
  representation = []
  while num > 0:
    representation.append(num % base)
    num //= base
  return representation == representation[::-1]

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./forward-and-backward.txt")) as file:
    num = parse_data(file.readlines())
    bases = [base for base in range(2, num + 1) if is_palindrome(num, base)]
    if len(bases) > 0:
      print(*bases)
    else:
      print("*")

main()
