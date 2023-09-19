import Foundation

let N = Int(readLine()!)!
var arr: [String] = []

for _ in 0..<N {
    let name = readLine()!.split(separator: ".")
    let format = String(name[1])
    arr.append(format)
}
arr.sort()

let set = Set(arr).sorted()
var result = Array(repeating: 0, count: set.count)
var index = 0

for i in arr {
    if set[index] == i {
        result[index] += 1
    } else {
        index += 1
        if set[index] == i {
            result[index] += 1
        }
    }
}

index = 0
for i in set {
    print("\(i) \(result[index])")
    index += 1
}