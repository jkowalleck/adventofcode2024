"""
all: a abc bcde de f

possibilities
- a bcde f
- abc def
- abc de f

towel: abcdef
"""

from Tools.scripts.ndiff import fopen


def parse_input(input_data):
  sections = input_data.strip().split("\n\n")
  towel_patterns = sections[0].split(", ")
  designs = sections[1].split("\n")
  return towel_patterns, designs


def can_form_design(patterns, design, memo):
  if design in memo:
    return memo[design]
  if design == "":
    return 1
  count = 0
  for pattern in patterns:
    if design.startswith(pattern):
      count += can_form_design(patterns, design[len(pattern):], memo)
  memo[design] = count
  return count


def count_possible_designs(towel_patterns, designs):
  total_count = 0
  memo = {}
  for design in designs:
    total_count += can_form_design(towel_patterns, design, memo)
  return total_count


# Example usage
input_data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

input_data = fopen('kow.txt').read()

towel_patterns, designs = parse_input(input_data)
total_arrangements = count_possible_designs(towel_patterns, designs)
print(f"Total number of ways to make each design: {total_arrangements}")
