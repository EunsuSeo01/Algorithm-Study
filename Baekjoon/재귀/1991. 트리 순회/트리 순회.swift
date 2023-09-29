import Foundation

let N = Int(readLine()!)!
var tree: [String:[String]] = [:]
var results: [String] = ["", "", ""]

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map { String($0) }
    
    tree.updateValue([input[1], input[2]], forKey: input[0])
}

func dfs(_ node: String) {
    if node == "." {
        return
    }
    
    results[0] += node
    dfs(tree[node]![0])
    results[1] += node
    dfs(tree[node]![1])
    results[2] += node
}

dfs("A")

for result in results {
    print(result)
}