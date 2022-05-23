import os
import requests

# Get all existing labels in the repository
all_existing_labels = []
response = requests.get('https://api.github.com/repos/wso2/api-manager/labels', headers={"Accept": "application/vnd.github.v3+json"})
if response.status_code == 200:
    for label in response.json():
        all_existing_labels.append(label["name"])
else:
    exit(0)

# Get suggested labels for the issue
i = os.environ["ISSUE_BODY"].index("### Affected Component") + 23
j = os.environ["ISSUE_BODY"].index("### Environment Details (with versions)")
suggested_labels = os.environ["ISSUE_BODY"][i:j].split(",")

# Verify whether suggested labels are existing in the repository
labels = []
for label in suggested_labels:
    affected_label = "Affected/" + label.strip()
    component_label = "Component/" + label.strip().split("-")[0]
    if affected_label in all_existing_labels:
        labels.append(affected_label)
    if component_label in all_existing_labels:
        labels.append(component_label)

# Return verified labels
if len(labels) > 0:
    print(",".join(labels))
else:
    print("Missing/Component")
