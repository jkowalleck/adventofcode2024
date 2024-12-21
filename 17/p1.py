


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
    if operand == 7:
      raise ValueError("Operand 7 is reserved and invalid.")
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
    elif opcode == 6:  # bdv
      B = A // (1 << get_combo_value(operand))
    elif opcode == 7:  # cdv
      C = A // (1 <<  get_combo_value(operand))
    else:
      raise ValueError(f"Unknown opcode {opcode}")
    pointer += 2

  return output

"""
# Example usage
initial_registers = [729, 0, 0]
program = [0, 1, 5, 4, 3, 0]
"""

initial_registers = [53437164, 0, 0]
program = [2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0]


output = run_program(initial_registers, program)
print(*output, sep=',')
