// Selection Sorting Algorithm:

public class insertionSort { 
    // Way 1:
    // ascending sort:
    public static void ascendingSort(int[] nums){
        for(int i = 1; i < nums.length; i++){
            int p1= i- 1, p2= i;
            while(p1>= 0 && nums[p1]> nums[p2]){
                swap(nums, p1--, p2--);
            }

            /*
             * int pointer= i;
             * for(int j= i- 1; j>= 0; j--){
             *      if(nums[j] > nums[pointer])
             *      swap(nums, j, pointer--);
             * }
             */
        }   
        System.out.print("Ascending Order: ");      
        print(nums);
    }
    
    // descending sort:
    public static void descendingSort(int[] nums){
        for(int i = 1; i < nums.length; i++){
            int p1= i- 1, p2= i;
            while(p1>= 0 && nums[p1]< nums[p2]){
                swap(nums, p1--, p2--);
            }
        } 
        System.out.print("Descending Order: ");    
        print(nums);
    }

    // Way 2:
    // ascending sort:
    public static void ascendingSort2(int[] nums){
        
    }
    
    // swap function:
    public static int[] swap(int[] nums, int index1, int index2){
        int temp = nums[index1]; 
        nums[index1] = nums[index2];
        nums[index2] = temp;
        
        return nums;
    }

    // print the array:
    public static void print(int[] nums){
        for(int num: nums){
            System.out.print(num + " ");
        }
        System.out.println("");        
    }

    public static void main(String[] args) {
        int[] arr= {4, 3, 4, 3, 2, 9, 8, 8, 6, 5, 1, 2, 10, 7};
        ascendingSort(arr);
        descendingSort(arr);
    }
}
