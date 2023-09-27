import Foundation

let N = Int(readLine()!)!
var input = readLine()!

var alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
var dict = Dictionary<String, Int>()
var arr: [Double] = []
var index = 0

for i in 0..<N {
    let num = Int(readLine()!)!
    dict[alphabets[i]] = num
}

for i in input {
    if i == "*" || i == "+" || i == "-" || i == "/" {
        let last = arr.popLast() ?? 0
        let secondLast = arr.popLast() ?? 0
        switch i {
        case "*":
            arr.append(secondLast * last)
        case "+":
            arr.append(secondLast + last)
        case "-":
            arr.append(secondLast - last)
        case "/":
            arr.append(secondLast / last)
        default:
            arr.append(0)
        }
    } else {
        arr.append(Double(dict[String(i)]!))
    }
}

print(String(format: "%.2f", arr[0]))