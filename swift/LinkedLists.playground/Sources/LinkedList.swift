
import UIKit

public class LinkedList {

    private var head: Node?
    private var count = 0
    
    public init() {}
    
    
    // MARK:  Push single value
    public func pushSingleValue(_ val: Int) {
        var current = head
        
        if current == nil {
            head = Node(val)
            self.count += 1
            return
        } else {
            
            while current!.next != nil {
                current = current!.next
                
            }
            
            current!.next = Node(val)
            self.count += 1
        }
        
    }
    
    // MARK:  Push multiple values
    public func pushMultipleValues(_ values: [Int]) {
        for val in values {
            self.pushSingleValue(val)
        }
    }
    
    // MARK:  Remove first value
    public func popFirstValue() {
        let current = head
        
        if current == nil {
            return
        } else if current!.next != nil {
            head = current!.next
        }
        
        self.count -= 1
    }
    
    // MARK:  Remove last value
    public func popLastValue() {
        
        var current = head
        
        if current == nil {
            return
        }
        
        while current!.next.next != nil {
            current = current!.next
        }
        
        current!.next = nil
        self.count -= 1
    }
    
    // MARK:  Delete item at index
    public func delete(at index: Int) {
        var current = head
        
        if index > self.count - 1 {
            return
        }
        
        if index == 0 {
            self.popFirstValue()
            return
        } else if index == self.count - 1 {
            self.popLastValue()
            return
        }
        
        for i in 0..<index {
            
            if i + 1 == index {
                current!.next = current!.next!.next
                self.count -= 1
                break
            } else {
                current = current!.next
            }
        }
        
    }
    
    // MARK:  Get specific value at index
    public func getValue(at index: Int) -> Int? {
        
        var current = head
        
        for _ in 0..<index {
            current = current!.next
        }
        
        return current!.data
    }
    
    // MARK:  Get total list count
    public func getListCount() -> Int {
        return count
    }
    
    // MARK:  See all values
    public func printAllValues() {
        var current = head
        
        while current!.next != nil {
            print(current!.data!)
            current = current!.next
        }
        print(current!.data!)
    }
    // MARK:  Get all values in array
    public func getAllValues() -> [Node] {
        
        var current = head
        var nodeArray = [Node]()
        
        while current!.next != nil {
            nodeArray.append(current!)
            current = current!.next
        }
        nodeArray.append(current!)
        return nodeArray
    }
    
}

