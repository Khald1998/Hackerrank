import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
        int positive_count = 0;
        int negative_count = 0;
        int zero_count = 0;
    
        int total_elements = arr.size();

        for(int i = 0 ; i<total_elements;i++){
            if (arr.get(i) > 0)
            {
                positive_count += 1;
            }
            else if (arr.get(i) < 0){
                negative_count += 1;
            } else{
                zero_count += 1;
            }
        
        
        
        }
            
        double positive_ratio = (double) positive_count / total_elements;
        double negative_ratio = (double) negative_count / total_elements;
        double zero_ratio = (double) zero_count / total_elements;

        // Print the ratios with 6 decimal places
        System.out.printf("%.6f%n", positive_ratio);
        System.out.printf("%.6f%n", negative_ratio);
        System.out.printf("%.6f%n", zero_ratio);

    
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
