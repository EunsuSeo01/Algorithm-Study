import Foundation

let T = Int(readLine()!)

for _ in 0..<T! {
    let chromosome = readLine()!
    let pattern = "^[A-F]?A+F+C+[A-F]?$"
    let regex = try? NSRegularExpression(pattern: pattern)
    if let _ = regex?.firstMatch(in: chromosome, options: [], range: NSRange(location: 0, length: chromosome.count)) {
        print("Infected!")
    } else {
        print("Good")
    }
}