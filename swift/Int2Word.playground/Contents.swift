import UIKit

let dict = [1: "one",2: "two",3: "three",4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20: "twenty",30: "thirty",40: "fourty",50: "fifty",60: "sixty",70: "seventy",80: "eighty",90: "ninety"]

let partition = ["hundred","thousand","million","billion"]

func intToWord(_ num: Int) -> String {
    
    var d = 100
    var w = ""
    var word = ""
    var dd = 100
    
    for part in partition {
        if dd <= num {
            d = dd
            w = part
        } else {
            break
        }
        dd *= 10
    }
    
    print(d,w)
    let s = Int(num / d)
    
    if let numStr = dict[s] {
        word = numStr + " " + w
    }
    
    let r = num % d
    
    print(num,s,r,word)
    return ""
}

print(intToWord(52526))

/*
 
 26 = twenty six
 520 = five hundred twenty
 
 500
 20
 
 12,537 = twelve thousand five hundred thirty seven
 12,000
 500
 30
 7
 
 hundred
 thousand
 million
 billion
 trillion
 */
