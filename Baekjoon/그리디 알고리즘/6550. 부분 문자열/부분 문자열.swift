import Foundation

while let input = readLine()?.split(separator: " ") {
    let s = input[0]
    var t = input[1]
    var isYes = true
    
    for i in s {
        if let index = t.firstIndex(of: i) {
            let range = t.startIndex...index
            t.removeSubrange(range)
        } else {
            isYes = false
            break
        }
    }
    
    isYes ? print("Yes") : print("No")
}