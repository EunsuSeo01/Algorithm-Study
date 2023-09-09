import Foundation

let A = Int(readLine()!)!
let T = Int(readLine()!)!
let signal = Int(readLine()!)!

var members: [Int] = []
for _ in 0..<A {
    members.append(0)
}

var times = 2
var index = 0
var num = 1

if signal == 0 {
    while true {
        if num == T {
            print(index % A)
            break
        }
        members[index%A] = num
        if num == T {
            print(index % A)
            break
        }
        num += 1
        members[(index+2)%A] = num
        if num == T {
            print((index+2)%A)
            break
        }
        num += 1
        index += 4
        for _ in 0..<times {
            members[index%A] = num
            if num == T {
                print(index % A)
                exit(0)
            }
            num += 1
            index += 1
        }
        index += times
        times += 1
    }
} else {
    while true {
        members[(index+1)%A] = num
        if num == T {
            print((index+1) % A)
            break
        }
        num += 1
        members[(index+3)%A] = num
        if num == T {
            print((index+3)%A)
            break
        }
        num += 1
        index += 4
        index += times
        for _ in 0..<times {
            members[index%A] = num
            if num == T {
                print(index % A)
                exit(0)
            }
            num += 1
            index += 1
        }
        times += 1
    }
}