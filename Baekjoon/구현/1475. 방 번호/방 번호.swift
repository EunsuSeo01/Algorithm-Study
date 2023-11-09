import Foundation

let N = readLine()!.map { String($0) }
var plasticNumSet = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
var num = 1

for i in N {
    if let index = plasticNumSet.firstIndex(of: i) {
        plasticNumSet.remove(at: index)
    } else {
        if i == "9" {
            if let index = plasticNumSet.firstIndex(of: "6") {
                plasticNumSet.remove(at: index)
                continue
            }
        } else if i == "6" {
            if let index = plasticNumSet.firstIndex(of: "9") {
                plasticNumSet.remove(at: index)
                continue
            }
        }
        num += 1
        plasticNumSet += ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        plasticNumSet.remove(at: plasticNumSet.firstIndex(of: i)!)
    }
}

print(num)