

def run_program(registers, program):
  A, B, C = registers
  pointer = 0
  output = []

  def get_combo_value(operand):
    if operand == 4:
      return A
    if operand == 5:
      return B
    if operand == 6:
      return C
    return operand

  plen = len(program)
  while pointer < plen:
    opcode = program[pointer]
    operand = program[pointer + 1]

    if opcode == 0:  # adv
      A = A // (1 << get_combo_value(operand))
    elif opcode == 1:  # bxl
      B ^= operand
    elif opcode == 2:  # bst
      B = get_combo_value(operand) % 8
    elif opcode == 3:  # jnz
      if A != 0:
        pointer = operand
        continue
    elif opcode == 4:  # bxc
      B ^= C
    elif opcode == 5:  # out
      output.append(get_combo_value(operand) & 7)
      if output != program[:len(output)]:
        return None
    elif opcode == 6:  # bdv
      B = A // (1 << get_combo_value(operand))
    elif opcode == 7:  # cdv
      C = A // (1 <<  get_combo_value(operand))
    pointer += 2

  return output

"""
# Example usage
registers = [729, 0, 0]
program = [0, 1, 5, 4, 3, 0]
"""

lowerbound = 35184372000000
upperbound = 290000000000000
registers = [lowerbound, 0, 0]
program = [2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0]

output = None
while (output:= run_program(registers, program)) != program:
  registers[0] += 1
  if registers[0] & 0xfffff == 0:
    print('register A:', registers[0])
print('final register A:', registers[0])
