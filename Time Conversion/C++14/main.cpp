#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string timeConversion(string s) {
    // Extract the AM or PM part from the time string
    string period = s.substr(8, 2);
    
    // Remove the AM or PM part to process time
    s = s.substr(0, 8);
    
    // Convert hour part to int
    int hour = stoi(s.substr(0, 2));
    
    // Convert to military time if necessary
    if (period == "PM" && hour != 12) {
        hour += 12;
    } else if (period == "AM" && hour == 12) {
        hour = 0;
    }
    
    // Convert back to string and add leading zero if necessary
    string hour_str = to_string(hour);
    if (hour < 10) {
        hour_str = "0" + hour_str;
    }
    
    // Replace the hour in the original string
    return hour_str + s.substr(2, 6);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = timeConversion(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
