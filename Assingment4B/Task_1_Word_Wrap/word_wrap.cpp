
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <climits>

using namespace std;

const long long INF = LLONG_MAX / 4;

int main() {
    int width;

    cout << "Enter maximum line width: ";
    cin >> width;

    cin.ignore();

    if (width <= 0) {
        cout << "Invalid line width.\n";
        return 1;
    }

    string sentence;

    cout << "Enter the text: ";
    getline(cin, sentence);

    stringstream ss(sentence);
    vector<string> words;
    string word;

    while (ss >> word) {
        if ((int)word.length() > width) {
            cout << "Error: Word '" << word
                 << "' exceeds the line width.\n";
            return 1;
        }

        words.push_back(word);
    }

    int n = words.size();

    if (n == 0) {
        cout << "No words provided.\n";
        return 0;
    }

    vector<long long> dp(n + 1, INF);
    vector<int> parent(n + 1, -1);

    dp[0] = 0;

    // Dynamic Programming
    for (int i = 1; i <= n; i++) {

        int lineLength = 0;

        for (int j = i; j >= 1; j--) {

            lineLength += words[j - 1].length();

            if (j < i) {
                lineLength++;
            }

            if (lineLength > width) {
                break;
            }

            int unusedSpaces = width - lineLength;

            long long penalty = 0;

            // Final line carries no penalty
            if (i != n) {
                penalty = 1LL * unusedSpaces * unusedSpaces;
            }

            long long currentCost = dp[j - 1] + penalty;

            if (currentCost < dp[i]) {
                dp[i] = currentCost;
                parent[i] = j - 1;
            }
        }
    }

    // Reconstruct optimal arrangement
    vector<pair<int, int>> lines;

    int position = n;

    while (position > 0) {
        int start = parent[position];

        if (start == -1) {
            cout << "No valid arrangement possible.\n";
            return 1;
        }

        lines.push_back({start, position - 1});
        position = start;
    }

    reverse(lines.begin(), lines.end());

    cout << "\n========== WORD WRAP RESULT ==========\n";

    cout << "Minimum Total Penalty = " << dp[n] << "\n";

    cout << "\nOptimal Line Arrangement:\n";

    for (int i = 0; i < (int)lines.size(); i++) {

        int start = lines[i].first;
        int end = lines[i].second;

        int lineLength = 0;

        cout << "\nLine " << i + 1 << ": ";

        for (int j = start; j <= end; j++) {
            cout << words[j];

            if (j < end) {
                cout << " ";
            }

            lineLength += words[j].length();
        }

        lineLength += (end - start);

        int unusedSpaces = width - lineLength;

        long long linePenalty = 0;

        if (i != (int)lines.size() - 1) {
            linePenalty = 1LL * unusedSpaces * unusedSpaces;
        }

        cout << "\nUnused Spaces = " << unusedSpaces;
        cout << "\nLine Penalty = " << linePenalty << "\n";
    }

    // Display DP states
    cout << "\n========== DP STATES ==========\n";

    cout << "DP[i] represents the minimum penalty "
         << "for arranging the first i words.\n\n";

    for (int i = 0; i <= n; i++) {
        cout << "DP[" << i << "] = " << dp[i] << "\n";
    }

    cout << "\n=====================================\n";

    return 0;
}
