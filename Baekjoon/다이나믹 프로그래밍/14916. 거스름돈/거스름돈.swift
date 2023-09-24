import Foundation

var n = Int(readLine()!)!
var answer = 0

while true {
    if n % 5 == 0 {
        answer += n / 5
        break
    } else {
        n -= 2
        answer += 1
    }
    
    if n < 0 {
        answer = -1
        break
    }
}

print(answer)