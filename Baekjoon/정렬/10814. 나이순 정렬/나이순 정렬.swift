let N = Int(readLine()!)!
var arr: [[String]] = []

for _ in 0..<N {
    arr.append(readLine()!.split(separator: " ").map {
        String($0)
    })
}

arr.sort { sec, fir in
    Int(sec[0])! < Int(fir[0])!
}

for i in arr {
    print(i.joined(separator: " "))
}