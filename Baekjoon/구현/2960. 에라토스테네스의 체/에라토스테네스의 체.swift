import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
var K = input[1]
var arr: [Int] = []

for i in 2...N {
    arr.append(i)
}

while K != 0 {
    let P = arr[0]
    let max = arr.last! / P
    arr.remove(at: 0)
    K -= 1
    if K == 0 {
        print(P)
        break
    }
    
    if max >= 2 {
        for i in 2...max {
            let mul = P * i
            if let index = arr.firstIndex(of: mul) {
                let num = arr[index]
                arr.remove(at: index)
                K -= 1
                if K == 0 {
                    print(num)
                    break
                }
            }
        }
    }
}