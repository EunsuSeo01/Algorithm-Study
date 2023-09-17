import Foundation

let N = Int(readLine()!)!
var aArr = readLine()!.split(separator: " ").map { Int($0)! }
let M = Int(readLine()!)!
var xArr = readLine()!.split(separator: " ").map { Int($0)! }

var intersectionSet = Set(aArr).intersection(Set(xArr))

for i in xArr {
    if let index = intersectionSet.firstIndex(of: i) {
        print(1)
    } else {
        print(0)
    }
}