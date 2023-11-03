import Foundation

let nums = readLine()!.split(separator: " ").map { Int($0)! }
let N = nums[0]
let M = nums[1]

let boardWhiteVer: [[Character]] = [
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"]
]
let boardBlackVer: [[Character]] = [
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
]
var inputBoard: [[Character]] = []
var answer = [Int]()

for _ in 0..<N {
    inputBoard.append(Array(readLine()!))
}

for x in 0..<N-7 {
    for y in 0..<M-7 {
        var board: [[Character]] = []
        for i in 0..<8 {
            board.append(Array(inputBoard[x + i][y..<y+8]))
        }
        answer.append(countRepaint(board))
    }
}

func countRepaint(_ board: [[Character]]) -> Int {
    var result1 = 0
    var result2 = 0
    
    // WBWB일 때 다시 칠해야 하는 정사각형 개수 count
    for i in 0..<8 {
        for j in 0..<8 {
            if boardWhiteVer[i][j] != board[i][j] {
                result1 += 1
            }
        }
    }
    // BWBW일 때 다시 칠해야 하는 정사각형 개수 count
    for i in 0..<8 {
        for j in 0..<8 {
            if boardBlackVer[i][j] != board[i][j] {
                result2 += 1
            }
        }
    }
    return min(result1, result2)
}

if answer.isEmpty {
    print(0)
} else {
    print(answer.min()!)
}