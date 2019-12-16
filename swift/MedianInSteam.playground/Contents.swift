
import Foundation


// Cyril Garcia
// 2/6/19
// Given an input stream of N integers the task is to insert integers to stream and print the median of the new stream formed by each insertion of X to the stream.

//  Example:
//  Flow in stream : 5, 15, 1, 3
//  5 goes to stream --> median 5 (5)
//  15 goes to stream --> median 10 (5, 15)
//  1 goes to stream --> median 5 (5, 15, 1)
//  3 goes to stream --> median 4 (5, 15, 1, 3)

func median(_ N: Int) -> Int? {
    
    var stream = [5, 15]
    stream.append(N)
    
    if stream.count > 2 {
        let sortedStream = stream.sorted()
        
        if sortedStream.count % 2 == 0 {
            let x = sortedStream.count / 2
            let y = x - 1
            
            let mean = (sortedStream[x] + sortedStream[y]) / 2
            return mean
        } else {
            return sortedStream[Int(stream.count / 2)]
        }
    } else {
        return (stream.first! + stream.last!) / 2
    }
}


let x = median(1)
print(x!)
