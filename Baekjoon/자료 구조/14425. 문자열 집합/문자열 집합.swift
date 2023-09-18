import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var S: [String] = []
for _ in 0..<N {
    S.append(readLine()!)
}
S.sort()

var checkedStrArr: [String] = []
for _ in 0..<M {
    checkedStrArr.append(readLine()!)
}

var answer = 0
func binarySearch(str: String) {
    var low = 0
    var high = S.count - 1
    
    while low <= high {
        let mid = (low + high) / 2
        if S[mid] == str {
            answer += 1
            break
        } else if S[mid] > str {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
}

for i in checkedStrArr {
    binarySearch(str: i)
}

print(answer)