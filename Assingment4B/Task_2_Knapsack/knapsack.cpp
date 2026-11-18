```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>

using namespace std;

struct Item {
    string id;
    int weight;
    int value;
    double ratio;
};

// Sort items by value-to-weight ratio
bool compareRatio(Item a, Item b) {
    return a.ratio > b.ratio;
}

// Fractional Knapsack using Greedy
void fractionalKnapsack(vector<Item> items, int capacity) {
    sort(items.begin(), items.end(), compareRatio);

    int remaining = capacity;
    double totalValue = 0;
    int operations = 0;

    cout << "\n========== FRACTIONAL KNAPSACK ==========\n";
    cout << "Capacity: " << capacity << "\n";

    cout << "\nDecision Sequence:\n";

    for (int i = 0; i < (int)items.size(); i++) {
        operations++;

        if (remaining == 0)
            break;

        if (items[i].weight <= remaining) {
            remaining -= items[i].weight;
            totalValue += items[i].value;

            cout << "Selected " << items[i].id
                 << " (100%)"
                 << " | Weight: " << items[i].weight
                 << " | Value: " << items[i].value << "\n";
        }
        else {
            double fraction =
                (double)remaining / items[i].weight;

            double gainedValue = fraction * items[i].value;

            totalValue += gainedValue;

            cout << "Selected " << items[i].id
                 << " (" << fraction * 100 << "%)"
                 << " | Weight used: " << remaining
                 << " | Value gained: " << gainedValue << "\n";

            remaining = 0;
        }
    }

    cout << "\nTotal Value = " << totalValue << "\n";
    cout << "Remaining Capacity = " << remaining << "\n";
    cout << "Items Examined = " << operations << "\n";
    cout << "Auxiliary Storage = O(n)\n";
}

// 0/1 Knapsack using Dynamic Programming
void zeroOneKnapsack(vector<Item> items, int capacity) {
    int n = items.size();

    vector<vector<int>> dp(
        n + 1, vector<int>(capacity + 1, 0)
    );

    int operations = 0;

    cout << "\n========== 0/1 KNAPSACK (DP) ==========\n";
    cout << "Capacity: " << capacity << "\n";

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            operations++;

            if (items[i - 1].weight <= w) {
                dp[i][w] = max(
                    dp[i - 1][w],
                    items[i - 1].value +
                    dp[i - 1][w - items[i - 1].weight]
                );
            }
            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << "\nDP Table (Maximum Value):\n";

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            cout << setw(5) << dp[i][w];
        }
        cout << "\n";
    }

    cout << "\nSelected Items:\n";

    int w = capacity;

    for (int i = n; i > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << "Selected " << items[i - 1].id
                 << " | Weight: " << items[i - 1].weight
                 << " | Value: " << items[i - 1].value << "\n";

            w -= items[i - 1].weight;
        }
    }

    cout << "\nMaximum Value = " << dp[n][capacity] << "\n";
    cout << "DP States Evaluated = " << operations << "\n";

    cout << "DP Table Memory = "
         << (n + 1) * (capacity + 1)
         << " integer cells\n";

    cout << "Time Complexity = O(n * Capacity)\n";
    cout << "Space Complexity = O(n * Capacity)\n";
}

// Demonstrate a case where ratio-based greedy fails for 0/1 Knapsack
void greedyCounterexample() {
    vector<Item> items = {
        {"A", 10, 60, 6.0},
        {"B", 20, 100, 5.0},
        {"C", 30, 120, 4.0}
    };

    int capacity = 50;

    cout << "\n\n========== GREEDY COUNTEREXAMPLE ==========\n";
    cout << "Capacity = 50\n";

    cout << "\nItems:\n";

    for (const Item& item : items) {
        cout << item.id
             << " | Weight: " << item.weight
             << " | Value: " << item.value
             << " | Ratio: " << item.ratio << "\n";
    }

    cout << "\nGreedy 0/1 Selection:\n";

    sort(items.begin(), items.end(), compareRatio);

    int remaining = capacity;
    int greedyValue = 0;

    for (const Item& item : items) {
        if (item.weight <= remaining) {
            remaining -= item.weight;
            greedyValue += item.value;

            cout << "Selected " << item.id << "\n";
        }
    }

    cout << "Greedy Total Value = " << greedyValue << "\n";

    zeroOneKnapsack(items, capacity);

    cout << "\nExpected Observation:\n";
    cout << "Greedy selects A and B, giving value 160.\n";
    cout << "DP selects B and C, giving optimal value 220.\n";
    cout << "The first greedy commitment is selecting A.\n";
}

int main() {
    int capacity;

    vector<Item> items = {
        {"A", 10, 60, 6.0},
        {"B", 20, 100, 5.0},
        {"C", 30, 120, 4.0}
    };

    cout << "========== KNAPSACK ALGORITHM ENGINE ==========\n";

    cout << "\nNormal Dataset:\n";

    for (const Item& item : items) {
        cout << item.id
             << " | Weight: " << item.weight
             << " | Value: " << item.value
             << " | Ratio: " << item.ratio << "\n";
    }

    cout << "\nEnter knapsack capacity: ";
    cin >> capacity;

    if (cin.fail() || capacity <= 0) {
        cout << "Invalid capacity.\n";
        return 1;
    }

    fractionalKnapsack(items, capacity);

    zeroOneKnapsack(items, capacity);

    greedyCounterexample();

    return 0;
}
```
