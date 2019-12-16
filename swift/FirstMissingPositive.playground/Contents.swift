import UIKit

//Given an unsorted integer array, find the smallest missing positive integer.

func firstMissingPositive(_ nums: [Int]) -> Int {
    var smallestNum = 1
    var mySet = Set<Int>()
    var i = 0

    while i < nums.count {
        
        let num = nums[i]
        
        if num > smallestNum {
            mySet.insert(num)
        } else if num == smallestNum {
            smallestNum += 1
        }
        
        if mySet.contains(smallestNum) {
            smallestNum += 1
        } else {
            i += 1
        }
    
    }
    
    return smallestNum
}
