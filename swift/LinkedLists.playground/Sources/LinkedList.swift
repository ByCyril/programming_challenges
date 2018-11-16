import UIKit

public class LinkedList {
    

    private var head: Node?
    private var count = 0
    
    public init() {
        
    }
    
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
    
    public func pushMultipleValues(_ values: [Int]) {
        for val in values {
            self.pushSingleValue(val)
        }
    }
    
    public func popFirstValue() {
        let current = head
        
        if current == nil {
            return
        } else if current!.next != nil {
            head = current!.next
        }
        
        self.count -= 1
    }
    
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
    
    public func delete(at index: Int) {
        var current = head
        
        if index - 1 > self.count {
            return
        }
        
        if index == 0 {
            self.popFirstValue()
            return
        } else if index == self.count {
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
    
    public func getListCount() -> Int {
        return count
    }
    
    public func printAllValues() {
        var current = head
        
        while current!.next != nil {
            print(current!.data!)
            current = current!.next
        }
        print(current!.data!)
    }
    
}

