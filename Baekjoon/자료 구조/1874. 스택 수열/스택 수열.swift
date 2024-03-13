import Foundation

let n = Int(readLine()!)!
var numbers: [Int] = []
var stack: [Int] = []
var target = 1
var result = ""

for _ in 0..<n {
    numbers.append(Int(readLine()!)!)
}

while true {
    if target > n {
        for n in stack.reversed() {
            if n == numbers[0] {
                numbers.removeFirst()
                result += "-\n"
            } else {
                result = "NO"
                break
            }
        }
        break
    } else {
        if !stack.isEmpty && numbers[0] == stack.last {
            result += "-\n"
            numbers.removeFirst()
            stack.removeLast()
        } else {
            result += "+\n"
            stack.append(target)
            target += 1
        }
    }
}

print(result)