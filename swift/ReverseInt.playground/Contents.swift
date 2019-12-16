import UIKit

//reverse a given integer

func reverse(_ x: Int) -> Int {
       
       var num = x

       if num < 0 {
           num *= -1
       }
       
       var rev = 0
       
       while num > 0 {
           let x = num % 10
           num /= 10
           rev *= 10
           rev += x
       }
       
       if rev > 2147483648 || rev < -2147483648 {
           return 0
       }
       
       if x < 0 {
           return rev * -1
       }
       
       return rev
   }
