import subprocess

executable = "./cloud_release_planner"

test_cases = [
    {
        "name": "Sample 1",
        "input": """3 50
Auth 10 60
Search 20 100
Payments 30 120
""",
        "expected": [
            "Greedy Value = 160",
            "Maximum Value = 220",
            "Selected = Search Payments",
            "Budget Used = 50"
        ]
    },
    {
        "name": "Sample 2",
        "input": """6 15
Cache 7 60
Search 4 36
Chat 8 33
Reports 5 34
Alerts 2 47
Backup 6 63
""",
        "expected": [
            "Greedy Value = 146",
            "Maximum Value = 170",
            "Selected = Cache Alerts Backup",
            "Budget Used = 15"
        ]
    },
    {
        "name": "Zero Budget",
        "input": """3 0
A 1 10
B 2 20
C 3 30
""",
        "expected": [
            "Greedy Value = 0",
            "Maximum Value = 0",
            "Selected = NONE",
            "Budget Used = 0"
        ]
    },
    {
        "name": "No Feature Fits",
        "input": """3 5
A 10 50
B 20 100
C 15 80
""",
        "expected": [
            "Greedy Value = 0",
            "Maximum Value = 0",
            "Selected = NONE",
            "Budget Used = 0"
        ]
    },
    {
        "name": "Every Feature Fits",
        "input": """3 20
A 3 10
B 5 20
C 4 15
""",
        "expected": [
            "Greedy Value = 45",
            "Maximum Value = 45",
            "Selected = A B C",
            "Budget Used = 12"
        ]
    },
    {
        "name": "Tied Optimal Values",
        "input": """3 10
A 5 10
B 6 10
C 4 10
""",
        "expected": [
            "Greedy Value = 20",
            "Maximum Value = 20",
            "Selected = A C",
            "Budget Used = 9"
        ]
    },
    {
        "name": "Single Feature",
        "input": """1 5
Only 5 9
""",
        "expected": [
            "Greedy Value = 9",
            "Maximum Value = 9",
            "Selected = Only",
            "Budget Used = 5"
        ]
    },
    {
        "name": "Zero Value Feature",
        "input": """3 10
A 3 0
B 4 20
C 5 30
""",
        "expected": [
            "Greedy Value = 50",
            "Maximum Value = 50",
            "Selected = B C",
            "Budget Used = 9"
        ]
    }
]

passed = 0

for test in test_cases:

    result = subprocess.run(
        [executable],
        input=test["input"],
        text=True,
        capture_output=True
    )

    actual = result.stdout.strip().splitlines()

    if result.returncode == 0 and actual == test["expected"]:

        print("[PASS]", test["name"])
        passed += 1

    else:

        print("[FAIL]", test["name"])
        print("Expected:", test["expected"])
        print("Actual:", actual)
        print("Error:", result.stderr)

print("\nTest Summary")
print("Total Tests:", len(test_cases))
print("Passed:", passed)
print("Failed:", len(test_cases) - passed)
