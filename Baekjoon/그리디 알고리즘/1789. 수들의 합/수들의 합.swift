import Foundation

var S = Int(readLine()!)!
var N = 1
var total = N

while true {
    if total > S {
        print(N-1)
        break
    } else if total == S {
        print(N)
        break
    } else {
        N += 1
        total += N
    }
}