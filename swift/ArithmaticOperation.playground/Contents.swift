import UIKit

/*
 Given a list of numbers and a target, see if there exist a combination of where you can add, subtract, or multiple the numbers to get the target.
 
 Example:
 Input: list = [1,2,3], target = 6
 Output true because 1 + 2 + 3 == 6 or 1 * 2 * 3 == 6
 */

func doesClick(_ list: [Int], _ target: Int) -> Bool {
    
    return doesClickHelper(list, target, list[0], 1)
}

func doesClickHelper(_ list: [Int], _ target: Int, _ currentTotal: Int, _ index: Int) -> Bool {
    
    if currentTotal == target {
        return true
    }
    
    if index >= list.count {
        return false
    }
    
    let sum = currentTotal + list[index]
    let diff = currentTotal - list[index]
    let prod = currentTotal * list[index]
    
    return doesClickHelper(list, target, sum, index + 1) || doesClickHelper(list, target, diff, index + 1) || doesClickHelper(list, target, prod, index + 1)
}
