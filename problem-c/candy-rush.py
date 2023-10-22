
def parse_data(data: list[str]):
  candies, members = [int(n) for n in data[0].split()]
  shelf = [int(n) for n in data[1].split()]
  if len(shelf) != candies:
    raise Exception("Invalid data")
  return members, shelf

def count_brands(brands: int, block: list[int]):
  return [block.count(brand) for brand in range(1, brands + 1)]

def max_candies(members: int, shelf: list[int]):
  max_candies = 0
  for i in range(len(shelf)):
    for j in range(i, len(shelf)):
      brands = count_brands(members, shelf[i:j+1])
      if brands.count(brands[0]) == len(brands) and len(brands) > max_candies:
        max_candies = len(brands) * brands[0]
  return max_candies

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./candy-rush.txt")) as file:
    members, shelf = parse_data(file.readlines())
    print(max_candies(members, shelf))

main()
