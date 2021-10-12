import argparse

parser = argparse.ArgumentParser(description='Add films to list.')
parser.add_argument('--film_name', type=str)
parser.add_argument('--stars', type=str)

args = parser.parse_args()
print(args)

with open("films.csv", "a") as f:
    f.write(f'\n{args.film_name}, {args.stars}')