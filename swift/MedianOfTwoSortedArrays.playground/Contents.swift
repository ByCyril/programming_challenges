import UIKit

/*
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
 
 example
 nums1 = [1, 2]
 nums2 = [3, 4]

 The median is (2 + 3)/2 = 2.5
*/

func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {

     var merged = [Int]()
    let a = nums1.count
    let b = nums2.count
    var i = 0
    var j = 0

    if nums1.isEmpty {
        merged.append(contentsOf: nums2)
        j = b
    } else if nums2.isEmpty {
        merged.append(contentsOf: nums1)
        i = a
    }

    while i != a || j != b {
        
        if (nums1[i] < nums2[j]) {
            merged.append(nums1[i])
            i += 1
        } else if (nums2[j] < nums1[i]) {
            merged.append(nums2[j])
            j += 1
        } else {
            merged.append(nums1[i])
            merged.append(nums2[j])
            i += 1
            j += 1
        }
        
        if (i == a) {
            merged.append(contentsOf: nums2[j..<b])
            break
        } else if (j == b) {
            merged.append(contentsOf: nums1[i..<a])
            break
        }
     
    }
    
    let len = merged.count
    
    if len % 2 == 0 {
        let midA = Int(Float(len / 2) + 0.5)
        let midB = Int(Float(len / 2) - 0.5)

        return Double(merged[midA] + merged[midB]) / 2.0
    } else {
        let mid = len / 2
        return Double(merged[mid])
    }
    
}

print(findMedianSortedArrays([1,2],[3,4]))

