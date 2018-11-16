import UIKit


let list = LinkedList()

list.pushMultipleValues([1,800,956,1432,11])

// Prints all the values
list.printAllValues()
print("")

// Gets all data
let allItems = list.getAllValues()
for item in allItems {
    print(item.data)
}

print("")

// Remove first and last elements
list.popFirstValue()
list.popLastValue()

// Gets the n - 1 elements. n = total number of elements
let singleVal = list.getValue(at: 5)
print(singleVal!)


