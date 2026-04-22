import os
import requests

# Get all existing labels in the repository
labels = []
all_existing_labels = []
response = requests.get('https://api.github.com/repos/wso2/api-manager/labels', headers={"Accept": "application/vnd.github.v3+json"})
if response.status_code == 200:
    for label in response.json():
        all_existing_labels.append(label["name"])
else:
    exit(0)

# Get affected component
component = None
i = os.environ["ISSUE_BODY"].find("### Affected Component")
j = os.environ["ISSUE_BODY"].find("### Version")

if i != -1 and j != -1 and j > i:
    component = os.environ["ISSUE_BODY"][i+23:j].strip()
    component_label = "Component/" + component
    if component_label in all_existing_labels:
        labels.append(component_label)

# Get component version
if j != -1:
    k = os.environ["ISSUE_BODY"].find("###", j + 11)
    if k != -1:
        version = os.environ["ISSUE_BODY"][j+11:k].strip()
    else:
        version = os.environ["ISSUE_BODY"][j+11:].strip()
        
    if component is not None:
        affected_label = "Affected/" + component + "-" + version
        if affected_label in all_existing_labels:
            labels.append(affected_label)

# Return verified labels
if len(labels) > 0:
    print(",".join(labels))
else:
    print("Missing/Component")
