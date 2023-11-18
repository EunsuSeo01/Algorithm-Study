import Foundation

var E = 1
var S = 1
var M = 1
var year = 1

let input = readLine()!.split(separator: " ").map { Int($0)! }

while true {
    if E == input[0] && S == input[1] && M == input[2] {
        print(year)
        break
    } else {
        E += 1
        S += 1
        M += 1
        
        if E > 15 {
            E = 1
        }
        if S > 28 {
            S = 1
        }
        if M > 19 {
            M = 1
        }
        
        year += 1
    }
}