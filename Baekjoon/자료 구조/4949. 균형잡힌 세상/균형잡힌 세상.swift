import Foundation

var stack: [Character] = []

while true {
    let input = readLine()!
    if input == "." {
        break
    }
    
    for target in input {
        if target == "(" || target == ")" || target == "[" || target == "]" {
            if (stack.last == "(" && target == ")") || (stack.last == "[" && target == "]") {
                stack.removeLast()
            } else {
                stack.append(target)
            }
        }
    }
    
    print(stack.isEmpty ? "yes" : "no")
    stack.removeAll()
}