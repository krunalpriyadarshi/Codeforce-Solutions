// Bubble Sorting Algorithm:
// Optimized by using boolean variable to check if the array is already sorted or not.

public class bubbleSort { 
    // ascending sort:
    public static void ascendingSort(int[] nums){
        for(int i = 0; i < nums.length; i++){
            boolean isSwapped = false;
            for(int j = i; j < nums.length; j++){
                if(nums[i] > nums[j]){
                    swap(nums, i, j);
                    isSwapped = true;
                }
            }
            // if no swap performed then break the loop.
            if(!isSwapped)
                break;
        }   
        System.out.print("Ascending Order: ");      
        print(nums);
    }
    
    // descending sort:
    public static void descendingSort(int[] nums){
        for(int i = 0; i< nums.length; i++){
            boolean isSwapped = false;
            for(int j= i; j< nums.length; j++){
                if(nums[i]< nums[j]){
                    swap(nums, i, j);
                    isSwapped = true;
                }
            }
            // if no swap performed then break the loop.
            if(!isSwapped)
                break;
        }
        System.out.print("Descending Order: ");    
        print(nums);
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
