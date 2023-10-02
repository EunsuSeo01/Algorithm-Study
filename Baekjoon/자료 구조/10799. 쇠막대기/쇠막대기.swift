import Foundation

var line = readLine()!.map { String($0) }
var stack = 0
var result = 0
var idx = 0

for i in line {
    if i == "(" {
        stack += 1
    } else {
        stack -= 1
        if line[idx-1] == "(" {
            result += stack
        } else {
            result += 1
        }
    }
    idx += 1
}

print(result)