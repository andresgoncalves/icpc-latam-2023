
def parse_data(data: list[str]):
  days, movies = [int(n) for n in data[0].split()]
  schedule = [int(n) for n in data[1].split()]
  if len(schedule) != days:
    raise Exception("Invalid data")
  return movies, schedule

def find_permutations(days: int, schedule: list[int], prev: list[int] = []):
  if len(prev) == days:
    i = 0
    for movie in schedule:
      if movie == prev[i]:
        i += 1
        if i == len(prev):
          return []
    return prev
  for movie in range(1, days + 1):
    if movie not in prev:
      new_prev = list(prev)
      new_prev.append(movie)
      result = find_permutations(days, schedule, new_prev)
      if len(result) > 0:
        return result
  return []

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./keen-on-order.txt")) as file:
    days, schedule = parse_data(file.readlines())
    result = find_permutations(days, schedule)
    if len(result) > 0:
      print(*result, sep=" ")
    else:
      print("*")

main()
