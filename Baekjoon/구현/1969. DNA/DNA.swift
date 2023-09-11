import Foundation

let input = readLine()!.split(separator: " ")
let N = Int(input[0])!
let M = Int(input[1])!
var DNAs: [String] = []

for _ in 0..<N {
    DNAs.append(readLine()!)
}

var resultDNA = ""
var resultNum = 0

for i in 0..<M {
    var ACGT = [0,0,0,0]
    let letters = ["A", "C", "G", "T"]
    for j in 0..<N {
        let t = DNAs[j].index(DNAs[j].startIndex, offsetBy: i)
        let letter = String(DNAs[j][t])
        switch letter {
        case letters[0]:
            ACGT[0] += 1
        case letters[1]:
            ACGT[1] += 1
        case letters[2]:
            ACGT[2] += 1
        case letters[3]:
            ACGT[3] += 1
        default:
            ACGT[0] += 1
        }
    }
    var letter = letters[0]
    var max = ACGT[0]
    var index = 0
    for acgt in ACGT {
        if acgt > max {
            max = acgt
            letter = letters[index]
        }
        index += 1
    }
    resultDNA.append(letter)
    resultNum += (N - max)
}
print(resultDNA)
print(resultNum)