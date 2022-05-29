import scala.collection.mutable.HashMap
object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {
        var hmap = new HashMap[Int, Int]()
        for(item <- nums ) {
            if ( !hmap.contains(item)) {
                hmap += (item -> 1)
            }else {
                return true
            }
        }
        false
    }
}
