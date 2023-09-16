import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
    let input = readLine()!.split(separator: " ")
    let N = Int(input[0])!
    var M = Int(input[1])!
    var result = 1 // 인덱스 M이 몇번째로 프린트 되는지
    
    var arr: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
    
    while !arr.isEmpty {
        if arr[0] == arr.max()! {
            if M == 0 {
                print(result)
                break
            }
            result += 1
        } else {
            arr.append(arr[0])
        }
        arr.remove(at: 0)
        
        M -= 1
        if M == -1 {
            M = arr.count-1
        }
    }
}