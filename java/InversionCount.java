//Given an array of integers. Objective is to find the inversion counts in the array
//Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

package arrays;

import java.util.Arrays;
import java.util.Scanner;

public class InversionCount {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long t = sc.nextLong();
		while(t-- >0) {
			long n = sc.nextLong();
			long arr[] = new long[(int)n];
			
			for(long i =0; i<n;i++) {
				arr[(int)i] = sc.nextLong();
			}
			System.out.println(inversionCount(arr, n));
		}
		sc.close();
	}
	
	static long inversionCount(long arr[], long N) {
		int n = (int)N;
		long inversions = mergeSortandCount(arr, 0, n-1);
		return inversions;
	}
	
	static long mergeSortandCount(long arr[], int l, int r) {
		long count  =0 ;
		if(r > l) {
			int m = l+(r-l)/2;
			count += mergeSortandCount(arr, l, m);
			count += mergeSortandCount(arr, m+1, r);
			count += mergeandCount(arr, l, m, r);
		}
		return count;
	}
	static long mergeandCount(long[] arr, int l, int m, int r) {
		long[] left = Arrays.copyOfRange(arr, l, m+1);
		long[] right = Arrays.copyOfRange(arr, m+1, r+1);
		int i =0, j=0, k = l;
		long swaps = 0;
		while(i < left.length && j <right.length) {
			if(left[i] <= right[j]) {
				arr[k++] = left[i++];
			}else { 
				arr[k++] = right[j++];
				swaps += (m+1)-(l+i);
			}
		}
		while(i < left.length) {
			arr[k++] = left[i++];
		}
		while(j < right.length) {
			arr[k++] = right[j++];
		}
		return swaps;
	}
}
