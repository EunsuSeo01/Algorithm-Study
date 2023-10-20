import Foundation

let N = readLine().map { Int($0)! }
var cards = readLine()!.split(separator: " ").map { Int($0)! }
let M = readLine().map { Int($0)! }
var numbers = readLine()!.split(separator: " ").map { Int($0)! }
var results: [Int] = []

cards.sort()

func binarySearch(_ num: Int, low: Int, high: Int) -> Int {
    let mid = (low + high) / 2
    if low > high {
        return 0
    }
    if num > cards[mid] {
        return binarySearch(num, low: mid + 1, high: high)
    } else if num == cards[mid] {
        return 1
    } else {
        return binarySearch(num, low: low, high: mid - 1)
    }
}
      
for num in numbers {
    results.append(binarySearch(num, low: 0, high: cards.count-1))
}

for result in results {
    print(result, terminator: " ")
}