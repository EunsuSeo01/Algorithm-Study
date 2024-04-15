import Foundation

let nums = readLine()!.split(separator: " ").map { Int($0)! }
var n = nums[0]
var m = nums[1]
var memo = [[String]](repeating: [String](repeating: "", count: 101), count: 101)

func pascalTriangle() {
    for i in 0...n {
        for j in 0...m {
            if j > i { break }
            if i == j || j == 0 {
                memo[i][j] = "1"
            }
            else {
                var sum = 0
                var res = ""
                var m1 = Array(memo[i-1][j-1]), m2 = Array(memo[i-1][j])
                while !m1.isEmpty || !m2.isEmpty || sum != 0 {
                    if !m1.isEmpty {
                        sum += Int(String(m1.removeLast())) ?? 0
                    }
                    if !m2.isEmpty {
                        sum += Int(String(m2.removeLast())) ?? 0
                    }
                    res.append(String(sum % 10))
                    sum /= 10
                }
                memo[i][j] = String(res.reversed())
            }
        }
    }
}

pascalTriangle()
print(memo[n][m])