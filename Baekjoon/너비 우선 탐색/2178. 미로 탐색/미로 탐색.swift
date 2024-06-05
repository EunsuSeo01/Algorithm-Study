let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0]
let M = input[1]

var graph: [[String]] = []
var visited = [[Bool]](repeating: [Bool](repeating: false, count: M), count: N)

let dx = [1, 0, -1, 0]
let dy = [0, 1, 0, -1]

for _ in 0..<N {
    graph.append(readLine()!.map { String($0) })
}

func isValidCoord(y: Int, x: Int) -> Bool {
    return 0..<N ~= y && 0..<M ~= x
}

func BFS(y: Int, x: Int) {
    var queue = [(y, x, 1)]
    var index = 0
    visited[y][x] = true
    
    while queue.count > index {
        let y = queue[index].0
        let x = queue[index].1
        let d = queue[index].2
        
        if y == N-1 && x == M-1 {
            print(d)
            break
        }
        
        for i in 0...3 {
            let ny = y + dy[i]
            let nx = x + dx[i]
            
            if isValidCoord(y: ny, x: nx) && graph[ny][nx] == "1" && !visited[ny][nx] {
                visited[ny][nx] = true
                queue.append((ny, nx, d + 1))
            }
        }
        index += 1
    }
}

BFS(y: 0, x: 0)