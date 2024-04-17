import Foundation

var N = Int(readLine()!)!

while N != 1 {
    for i in 2...N {
        if N % i == 0 {
            print(i)
            N = Int(N / i)
            break
        }
    }
}