
def parse_data(data: list[str]):
  string = data[0].strip()
  times = int(data[1])
  return string, times

def compute_matrix(string: str):
  matrix = [
    [
      "X" if not string[i] > string[j] else
      "!" if not i < j else
      "*"
      for i in range(len(string))
    ]
    for j in range(len(string))
  ]
  return matrix

def calculate_inversions(string: str, times: int):
  matrix = compute_matrix(string)
  total = 0
  mod = 10**9 + 7
  for vector in matrix:
    repeat = sum(range(1, times))
    total = (total + (repeat + times) * vector.count("*") + repeat * vector.count("!")) % mod
  return total

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./inversions.txt")) as file:
    string, times = parse_data(file.readlines())
    print(calculate_inversions(string, times))

main()

