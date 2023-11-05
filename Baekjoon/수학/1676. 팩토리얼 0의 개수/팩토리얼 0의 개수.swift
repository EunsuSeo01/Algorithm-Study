import Foundation

let N = Int(readLine()!)!
var answer = 0

answer += N / 125
answer += N / 25
answer += N / 5

print(answer)