class BinarySearch {
    int binarySearch(int a[], int l, int r, int x)
    {
        while (l <= r) {
            int mid = (l + r) / 2;//middle element
            if (a[mid] == x) {
                return mid;
            // If element is smaller than mid, then it can only be present in left subarray            
            } 
            else if (a[mid] > x) {
                r = mid - 1;// we decrease our r pointer to mid - 1 
            }
            // Else the element can only be present in right subarray             
             else {
              l = mid + 1;// so we increase our l pointer to mid + 1
            }  
        }

        // If no element found output will be -1
        return -1;
    }

    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();

        int a[] = { 2, 3, 4, 10, 40 };
        int n = a.length;
        int x = 10;
      
        int res = ob.binarySearch(a, 0, n - 1, x);

        if (res == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + res);
    }
}
