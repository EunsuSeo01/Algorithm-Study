import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var flags = Array(repeating: false, count: N + 1)
var depth = 0
var res: [Int] = []

func dfs(depth: Int) {
    if depth == M {
        if res.sorted() == res {
            print(
                res.map {
                    String($0)
                }.joined(separator: " ")
            )
        }
        return
    }
    
    for i in 1...N {
        if !flags[i] {
            flags[i] = true
            res.append(i)
            dfs(depth: depth + 1)
            flags[i] = false
            res.removeLast()
        }
    }
}

dfs(depth: depth)