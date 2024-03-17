import Foundation

let N = Int(readLine()!)!
var result = 0
var stack: [Character]

for _ in 0..<N {
    stack = []
    var letter = readLine()!
    if letter.count % 2 == 0 {
        let ALetter = letter.filter { character in
            character == "A"
        }
        if ALetter.count % 2 == 0 {
            for l in letter {
                if stack.last == l {
                    stack.removeLast()
                } else {
                    stack.append(l)
                }
                letter.removeFirst()
            }
            if stack.isEmpty {
                result += 1
            }
        }
    }
}

print(result)