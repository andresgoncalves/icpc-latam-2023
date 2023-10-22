
def parse_data(data: list[str]):
  n_towers = int(data[0])
  towers = [
    tuple([int(n) for n in tower.split()])
    for tower in data[1:]
  ]
  if len(towers) != n_towers:
    raise Exception("Invalid data")
  return towers

def get_points(tower: tuple[int,int,int]):
  tx, ty, tr = tower
  points = set()
  for n in range(tr + 1):
    points.add((tx - (tr - n), ty - n))
    points.add((tx - (tr - n), ty + n))
    points.add((tx + (tr - n), ty - n))
    points.add((tx + (tr - n), ty + n))
  return points

def get_coordinates(towers: list[int]):
  coords = get_points(towers[0])
  for tower in towers[1:]:
    coords = coords.intersection(get_points(tower))
  return sorted(coords, key=lambda coord: coord[0] * 10000 + coord[1])

def main():
  from pathlib import Path
  with open(Path(__file__).parent.joinpath("./gps-on-a-flat-earth.txt")) as file:
    towers = parse_data(file.readlines())
    print(*[f"{coord[0]} {coord[1]}" for coord in get_coordinates(towers)], sep="\n")

main()
