// Return the number of occurences of each character in a given string
// Example: "aabc" -> a = 2, b = 1, c = 1

// *** HINT ***
// Use a dictionary of type [Character : Int]

import UIKit

func mostRepeatedCharacter(str: String) {
    
    // Create your dictionary of type [Character : Int]
    var counter = [Character : Int]()
    
    // Iterate through each character in the string
    for c in str.characters {
        
        // If counter[c] exists, get the count
        if let count = counter[c] {
            // get the count and increment by 1
            counter[c] = count + 1
        } else {
            // Otherwise, set it to 1
            counter[c] = 1
        }
    }
    
    // Print your values
    print(counter.values)
}

mostRepeatedCharacter(str: "aabc")
