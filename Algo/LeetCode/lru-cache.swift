import Foundation

class Node {
  var val: Int
  init(v: Int) {
    val = v
  }

  var next: Node?
  var previous: Node?
}

class LL {
  let head: Node = {
    let n = Node(v: -1)
    n.previous = n
    n.next = n
    return n
  }()

  func insertInFront(node: Node) {
    let x = head.next
    x?.previous = node
    head.next = node
    node.previous = head
    node.next = x
    length += 1
  }

  func bringToFront(node: Node) {
    node.previous?.next = node.next
    node.next?.previous = node.previous
    length -= 1
    insertInFront(node: node)
  }

  func deleteLast() -> Node? {
    let x = head.previous
    head.previous?.previous?.next = head
    head.previous = head.previous?.previous
    length -= 1
    return x
  }

  var length = 0

}

class LRUCache {

  var dd = [Int: Node]()
  let ll = LL()
  let capacity: Int

  init(_ capacity: Int) {
    self.capacity = capacity
  }

  func get(_ key: Int) -> Int {
    guard let x = dd[key] else {
      return -1
    }
    ll.bringToFront(node: x)
    // bring x.nn to front of list
    return x.val
  }

  func put(_ key: Int, _ value: Int) {
    guard let x = dd[key] else {
      if ll.length == capacity { // check if at capacity
        let rn = ll.deleteLast()! // delete last node from list
        dd.removeValue(forKey: rn.val)
      }
      let node = Node(v: value)
      ll.insertInFront(node: node)
      // put node in front of list
      dd[key] = node
      return
    }
    x.val = value
    ll.bringToFront(node: x)
    // put node in front of list
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache(capacity)
 * let ret_1: Int = obj.get(key)
 * obj.put(key, value)
 */

let obj = LRUCache(2)
let ret_1: Int = obj.get(1)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
obj.get(2)
obj.put(4, 4)
obj.get(1)
obj.get(3)
obj.get(4)
