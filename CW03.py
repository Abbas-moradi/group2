import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--name', required=True, type=str)
parser.add_argument('--lname', required=True, type=str)
parser.add_argument('--age', type=int)

args = parser.parse_args()

print(f'Hello {args.name} {args.lname}, your age is {args.age}')