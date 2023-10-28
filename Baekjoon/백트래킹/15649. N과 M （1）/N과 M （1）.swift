import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var ans: [Int] = []

func backTracking() {
    if ans.count == M { // 배열의 길이를 확인
        for a in ans {
            print(a, terminator: " ") // 1 2 3 이런 상태로 출력하기 위해
        }
        print()
        return
    }
    for i in 1...N { // 1 ~ N 까지
        if !ans.contains(i) { // 중복 확인
            ans.append(i) // 배열 추가
            backTracking() // 재귀
            ans.removeLast() // back()에서 return으로 돌아오면 이 부분이 실행됨. 1,2 3일 때 3을 제거해서 전 단계로 돌아가는 것
        }
    }
}

backTracking()