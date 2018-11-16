//: Playground - noun: a place where people can play

import UIKit

let coordinates = [[1, 2], [3, 3], [1, 1], [5, 1], [-1, 4]]



func distanceFromOrigin(points: [[Int]]) {
    
    var shortestDistance = 100.0
    var shortestCoord = [Int]()
    for point in points {
        let x = Double(point[0])
        let y = Double(point[1])
        let d = sqrt((x * x) + (y * y))
        
        if d < shortestDistance {
            shortestDistance = d
            shortestCoord.removeAll()
            shortestCoord.append(contentsOf: point)
            
        }
    }
    
    print(shortestCoord)
}

func distanceFromPoint(points: [[Int]], point: [Int]) {
    
    let x1 = Double(point[0])
    let y1 = Double(point[1])
    
    var shortestDistance = 100.0
    var shortestCoord = [Int]()
    
    for coord in points {
        let x2 = Double(coord[0])
        let y2 = Double(coord[1])
        let d = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

        if d < shortestDistance {
            shortestDistance = d
            shortestCoord.removeAll()
            shortestCoord.append(contentsOf: coord)
            
        }
    }
    print(shortestCoord)
}

distanceFromOrigin(points: coordinates)
distanceFromPoint(points: coordinates, point: [0, -1])
