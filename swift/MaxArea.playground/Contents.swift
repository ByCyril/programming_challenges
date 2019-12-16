import UIKit

/*
 Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

 Note: You may not slant the container and n is at least 2.
 */
func maxArea(_ height: [Int]) -> Int {
    var i = 0
    var j = height.count - 1
    var max = 0
    var base = height.count - 1
    
    while i < j {
        let a = height[i]
        let b = height[j]
        
        var h: Int!
        
        if a < b {
            h = a
            i += 1
        } else {
            h = b
            j -= 1
        }
        
        let area = base * h
        base -= 1
        
        if area > max {
            max = area
        }
    }
    
    return max
}

print(maxArea([1,8,6,2,5,4,8,3,7]))
