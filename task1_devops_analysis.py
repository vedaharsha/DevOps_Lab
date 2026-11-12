
# TASK 1: ADVANTAGES AND BUSINESS IMPACT OF DEVOPS

print("=" * 60)
print("ADVANTAGES AND BUSINESS IMPACT OF DEVOPS")
print("=" * 60)

metrics = {
    "Deployment Frequency (per month)": (2, 20),
    "Lead Time (hours)": (120, 4),
    "Change Failure Rate (%)": (20, 5),
    "Recovery Time (hours)": (8, 0.5),
    "Manual Deployment Effort (hours)": (10, 2),
    "Customer Satisfaction (%)": (65, 90)
}

print("\nBEFORE AND AFTER DEVOPS IMPLEMENTATION\n")

for metric, values in metrics.items():
    before, after = values

    print(metric)
    print("Before DevOps:", before)
    print("After DevOps :", after)

    if metric == "Deployment Frequency (per month)":
        print("Result: Deployment frequency increased")
    elif metric == "Customer Satisfaction (%)":
        print("Result: Customer satisfaction improved")
    else:
        print("Result: Performance improved through reduction")

    print("-" * 45)

print("\nKEY ADVANTAGES OF DEVOPS")

advantages = [
    "Faster software releases",
    "Improved collaboration",
    "Automated testing",
    "Reduced application downtime",
    "Faster error recovery",
    "Improved customer satisfaction"
]

for advantage in advantages:
    print("-", advantage)

print("\nDevOps evaluation completed successfully.")
