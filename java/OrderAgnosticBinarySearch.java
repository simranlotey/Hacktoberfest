public class OrderAgnosticBinarySearch {
    static int binarySearch(int[] arr, int target){
        boolean isAsc=arr[0]<arr[arr.length-1];

        int start=0, end= arr.length-1;
        while(start<=end){
            int mid=start+(end-start)/2;
            if(arr[mid]==target) return mid;

            if(isAsc){
                if(target>arr[mid]) start=mid+1;
                else end=mid-1;
            }
            else{
                if(target<arr[mid]) start=mid+1;
                else end=mid-1;
            }
        }
        return (isAsc?--end:++end);
    }
}