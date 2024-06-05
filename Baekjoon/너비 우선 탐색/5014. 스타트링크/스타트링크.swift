let input = readLine()!.split(separator: " ").map{ Int(String($0))! }

let f = input[0]
let s = input[1]
let g = input[2]
let u = input[3]
let d = input[4]

var isStair = true

func BFS() {
    var queue = [(Int, Int)]()
    var visited = Array(repeating: false, count: 1000001)
    
    queue.append((s, 0))
    visited[s] = true
    
    while !queue.isEmpty {
        let pop = queue.removeFirst()
        if pop.0 == g {
            isStair = false
            print(pop.1)
            break
        }
        
        if pop.0 + u <= f && !visited[pop.0 + u] {
            queue.append((pop.0 + u, pop.1 + 1))
            visited[pop.0 + u] = true
        }
        if pop.0 - d > 0 && !visited[pop.0 - d] {
            queue.append((pop.0 - d, pop.1 + 1))
            visited[pop.0 - d] = true
        }
    }
    
    if isStair {
        print("use the stairs")
    }
}

BFS()