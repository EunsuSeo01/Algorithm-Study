import Foundation

var N = Int(readLine()!)!
var nDict = Dictionary(readLine()!.split(separator: " ").map { (Int($0)!, 1) }, uniquingKeysWith: +)

var M = Int(readLine()!)!
var mArr: [Int] = readLine()!.split(separator: " ").map { Int($0)! }

for i in mArr {
    print(nDict[i, default: 0], terminator: " ")
}