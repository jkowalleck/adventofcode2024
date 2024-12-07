def input = [
  'sanple' : '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20''',
  'kow' : '''190: 10 19
3267: 81 40 27''' // Example data for 'kow', since original code references 'kow'
]

def who = 'kow'
def data = input[who] ?: ''
def calibrations = data.split('\n')*.split(': ')

calibrations.retainAll { cal ->
    if (cal.size() < 2) return false // Skip malformed lines

    def res = cal[0].toBigDecimal()
    def poss = cal[1].split(' ')*.toBigDecimal()

    def n = poss.size() - 1
    if (n < 1) {
        // If there's only one value, just check if it's equal to res
        return poss[0] == res
    }

    def totalCombinations = 3**n
    def found = false

    outer: for (def i = 0; i < totalCombinations; i++) {
        def temp = i
        def acc = poss[0]

        // Apply operations corresponding to the base-3 representation of i
        for (int j = 1; j < poss.size(); j++) {
            def opDigit = temp % 3
            temp = temp.intdiv(3)
            def val = poss[j]

            switch (opDigit) {
                case 0: // '+'
                    acc = acc + val
                    break
                case 1: // '*'
                    acc = acc * val
                    break
                case 2: // '|', concatenation
                    acc = (acc.toString() + val.toString()).toBigDecimal()
                    break
            }
        }

        if (acc == res) {
            found = true
            break outer
        }
    }

    return found
}

println("Remaining cals (${calibrations.size()}):\n$calibrations")
println("Sum of all valid results: ${calibrations*.getAt(0)*.toBigDecimal().sum()}")
