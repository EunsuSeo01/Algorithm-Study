import Foundation

var squareColors: [[Int]] = []

var N = Int(readLine()!)!
for _ in 0..<N {
    squareColors.append(readLine()!.split(separator: " ").map { Int($0)! })
}
var white = 0
var blue = 0

func getColor(arr: [[Int]], len: Int) -> Int? {
    let prev = arr[0][0]
    for i in 0..<len {
        for j in 0..<len {
            if prev != arr[i][j] {
                // 다른 색
                return nil
            }
        }
    }
    // 같은 색
    return prev
}

func divide(arr: [[Int]], rStart: Int, rEnd: Int, cStart: Int, cEnd: Int) -> [[Int]] {
    var newArr: [[Int]] = []
    for i in rStart..<rEnd {
        var line: [Int] = []
        for j in cStart..<cEnd {
            line.append(arr[i][j])
        }
        newArr.append(line)
    }
    return newArr
}

func recursive(arr: [[Int]], len: Int) {
    if let color = getColor(arr: arr, len: len) {
        if color == 1 {
            blue += 1
        } else {
            white += 1
        }
    } else {
        let arr11 = divide(arr: arr, rStart: 0, rEnd: len/2, cStart: 0, cEnd: len/2)
        let arr12 = divide(arr: arr, rStart: 0, rEnd: len/2, cStart: len/2, cEnd: len)
        let arr21 = divide(arr: arr, rStart: len/2, rEnd: len, cStart: 0, cEnd: len/2)
        let arr22 = divide(arr: arr, rStart: len/2, rEnd: len, cStart: len/2, cEnd: len)
        recursive(arr: arr11, len: len/2)
        recursive(arr: arr12, len: len/2)
        recursive(arr: arr21, len: len/2)
        recursive(arr: arr22, len: len/2)
    }
}

recursive(arr: squareColors, len: N)

print(white)
print(blue)