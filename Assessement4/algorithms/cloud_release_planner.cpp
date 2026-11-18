#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Feature {
    string name;
    int cost;
    int value;
};

// GREEDY ALGORITHM
int calculateGreedyValue(
    const vector<Feature>& features, int budget) {

    vector<int> order(features.size());

    for (int i = 0; i < (int)features.size(); i++) {
        order[i] = i;
    }

    // Sort by decreasing value-to-cost ratio
    stable_sort(order.begin(), order.end(),
        [&](int a, int b) {

            long long left =
                1LL * features[a].value * features[b].cost;

            long long right =
                1LL * features[b].value * features[a].cost;

            return left > right;
        });

    int totalValue = 0;
    int remainingBudget = budget;

    for (int index : order) {

        if (features[index].cost <= remainingBudget) {

            remainingBudget -= features[index].cost;
            totalValue += features[index].value;
        }
    }

    return totalValue;
}

// MAIN FUNCTION
int main() {

    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W;
    cin >> n >> W;

    vector<Feature> features(n);

    // INPUT
    for (int i = 0; i < n; i++) {

        cin >> features[i].name
            >> features[i].cost
            >> features[i].value;
    }

    // STEP 1: GREEDY VALUE
    int greedyValue = calculateGreedyValue(features, W);

    // STEP 2: INITIALIZE DP TABLE
    vector<vector<int>> dp(
        n + 1, vector<int>(W + 1, 0)
    );

    // STEP 3: DYNAMIC PROGRAMMING
    for (int i = 1; i <= n; i++) {

        int cost = features[i - 1].cost;
        int value = features[i - 1].value;

        for (int w = 0; w <= W; w++) {

            // Exclude current feature
            dp[i][w] = dp[i - 1][w];

            // Include current feature if it fits
            if (cost <= w) {

                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - cost]
                );
            }
        }
    }

    // STEP 4: MAXIMUM VALUE
    int maximumValue = dp[n][W];

    // STEP 5: MINIMUM BUDGET FOR MAXIMUM VALUE
    int budgetUsed = 0;

    while (budgetUsed <= W &&
           dp[n][budgetUsed] != maximumValue) {
        budgetUsed++;
    }

    // STEP 6: RECONSTRUCT SELECTED FEATURES
    vector<string> selected;

    int remainingBudget = budgetUsed;

    for (int i = n; i >= 1; i--) {

        if (dp[i][remainingBudget] !=
            dp[i - 1][remainingBudget]) {

            selected.push_back(features[i - 1].name);

            remainingBudget -= features[i - 1].cost;
        }
    }

    // Restore original input order
    reverse(selected.begin(), selected.end());

    // STEP 7: OUTPUT
    cout << "Greedy Value = " << greedyValue << '\n';

    cout << "Maximum Value = " << maximumValue << '\n';

    cout << "Selected = ";

    if (selected.empty()) {
        cout << "NONE";
    }
    else {
        for (int i = 0; i < (int)selected.size(); i++) {

            if (i > 0) cout << " ";

            cout << selected[i];
        }
    }

    cout << '\n';

    cout << "Budget Used = " << budgetUsed << '\n';

    return 0;
}
