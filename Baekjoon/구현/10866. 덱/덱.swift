let num = readLine().map { Int($0) }
var arr = [Int]()
for _ in 1...num!! {
    let input = readLine()!.split(separator: " ")
    switch input[0] {
    case "push_back":
        arr.append(Int(input[1])!)
    case "push_front":
        arr = [Int(input[1])!] + arr
    case "front":
        print(arr.isEmpty ? -1 : arr[0])
    case "back":
        print(arr.isEmpty ? -1 : arr[arr.count - 1])
    case "size":
        print(arr.count)
    case "empty":
        print(arr.isEmpty ? 1 : 0)
    case "pop_front":
        if arr.isEmpty {
            print(-1)
        } else {
            let firstIndex = 0
            print(arr[firstIndex])
            arr.remove(at: firstIndex)
        }
    case "pop_back":
        if arr.isEmpty {
            print(-1)
        } else {
            let lastIndex = arr.count - 1
            print(arr[lastIndex])
            arr.remove(at: lastIndex)
        }
    default:
        print()
    }
}