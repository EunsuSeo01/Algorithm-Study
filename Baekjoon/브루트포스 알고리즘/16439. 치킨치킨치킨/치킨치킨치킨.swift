import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var preferArr: [[Int]] = []
var chickenArr: [Int] = []
var threeChickenCombi: [[Int]] = []

for _ in 0..<N {
    let nums = readLine()!.split(separator: " ").map { Int($0)! }
    preferArr.append(nums)
}
for i in 0..<M {
    chickenArr.append(i)
}

func combination<T: Comparable>(_ array: [T], _ n: Int) -> [[T]] {
    var result = [[T]]()
    if array.count < n { return result }

    func cycle(_ index: Int, _ now: [T]) {
        if now.count == n {
            result.append(now)
            return
        }
        
        for i in index..<array.count {
            cycle(i + 1, now + [array[i]])
        }
    }
    
    cycle(0, [])
    
    return result
}

threeChickenCombi = combination(chickenArr, 3)

var maxSum = 0
for i in threeChickenCombi {
    var currentSum = 0
    for j in 0..<N {
        currentSum += [ preferArr[j][i[0]], preferArr[j][i[1]], preferArr[j][i[2]] ].max()!
    }
    if currentSum > maxSum {
        maxSum = currentSum
    }
}

print(maxSum)