import Foundation

let N = Int(readLine()!)!
var arr = [Int]()
var removedNum = Int(exactly: round(Double(N) * 0.15))!
for _ in 0..<N {
    arr.append(Int(readLine()!)!)
}
arr.sort()

var arrSlice = arr[removedNum..<arr.count-removedNum]
if arrSlice.isEmpty {
    print(0)
} else {
    print(Int(exactly: round(Double(arrSlice.reduce(0,+))/Double(arrSlice.count)))!)
}