import Foundation

let n = Int(readLine()!)!
let k = Int(readLine()!)!
var arr: [String] = []
var results: Set<String> = []
var iIdx = 0
var jIdx = 0
var kIdx = 0
var zIdx = 0


for _ in 0..<n {
    arr.append(readLine()!)
}

if k == 2 {
    for i in arr {
        jIdx = 0
        for j in arr {
            if iIdx != jIdx {
                var str = ""
                str += i + j
                results.insert(str)
            }
            jIdx += 1
        }
        iIdx += 1
    }
} else if k == 3 {
    for i in arr {
        jIdx = 0
        for j in arr {
            kIdx = 0
            for k in arr {
                if iIdx != jIdx && jIdx != kIdx && iIdx != kIdx {
                    var str = ""
                    str += i + j + k
                    results.insert(str)
                }
                kIdx += 1
            }
            jIdx += 1
        }
        iIdx += 1
    }
} else {
    for i in arr {
        jIdx = 0
        for j in arr {
            kIdx = 0
            for k in arr {
                zIdx = 0
                for z in arr {
                    if iIdx != jIdx 
                        && jIdx != kIdx
                        && iIdx != kIdx
                        && iIdx != zIdx
                        && kIdx != zIdx
                        && jIdx != zIdx
                    {
                        var str = ""
                        str += i + j + k + z
                        results.insert(str)
                    }
                    zIdx += 1
                }
                kIdx += 1
            }
            jIdx += 1
        }
        iIdx += 1
    }
}

print(results.count)