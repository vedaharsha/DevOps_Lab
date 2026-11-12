
# TASK 2: MERGE CONFLICTS AND RESOLUTION

print("=" * 55)
print("GIT MERGE CONFLICT DEMONSTRATION")
print("=" * 55)

developer1 = {
    "developer": "Developer 1",
    "feature": "Payment Functionality"
}

developer2 = {
    "developer": "Developer 2",
    "feature": "Order Tracking Functionality"
}

print("\nDeveloper 1 Changes:")
print(developer1)

print("\nDeveloper 2 Changes:")
print(developer2)

print("\nCAUSE OF MERGE CONFLICT:")
print("Both developers modified the same file")
print("in different branches.")

print("\nRESOLUTION PROCEDURE:")
steps = [
    "Identify conflicting files using Git",
    "Open the file containing conflict markers",
    "Review both developers' changes",
    "Combine or select the required changes",
    "Remove conflict markers",
    "Stage the resolved file",
    "Commit the resolved changes"
]

for index, step in enumerate(steps, start=1):
    print(f"{index}. {step}")

print("\nPREVENTION PRACTICES:")
practices = [
    "Frequent commits",
    "Regular pulling from main branch",
    "Small feature branches",
    "Team communication",
    "Early conflict resolution"
]

for practice in practices:
    print("-", practice)

print("\nMerge conflict analysis completed.")
