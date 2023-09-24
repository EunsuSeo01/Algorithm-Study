import Foundation

let poly = ["AAAA", "BB"]
var input = readLine()!
var x = ""
var answer = ""

func polynomino(str: String) -> String {
    let n = str.count
    if n % 2 == 1 {
        return str
    }
    return String(repeating: poly[0], count: n / 4) + String(repeating: poly[1], count: (n % 4) / 2)
}

for i in input {
    if i == "." {
        answer += polynomino(str: x)
        answer += String(i)
        x = ""
        continue // 이 아래 실행 안 되고 넘어감
    }
    x += String(i)
}

answer += polynomino(str: x)
print(answer.contains("X") ? -1 : answer)