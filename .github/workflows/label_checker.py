import os
import re
import requests

# Get all existing labels in the repository (paginated)
all_existing_labels = []
page = 1
while True:
    response = requests.get(
        'https://api.github.com/repos/wso2/api-manager/labels',
        headers={"Accept": "application/vnd.github.v3+json"},
        params={"per_page": 100, "page": page}
    )
    if response.status_code != 200:
        exit(0)
    page_labels = response.json()
    if not page_labels:
        break
    all_existing_labels.extend(label["name"] for label in page_labels)
    page += 1


def extract_section(body, heading):
    match = re.search(re.escape(heading) + r"\s*\n+(.*?)(?=\n### |\Z)", body, re.DOTALL)
    return match.group(1).strip() if match else None


labels = []
issue_body = os.environ["ISSUE_BODY"]

# Get affected component (not all issue templates have this section)
component = extract_section(issue_body, "### Affected Component")
if component:
    component_label = "Component/" + component
    if component_label in all_existing_labels:
        labels.append(component_label)

    # Get component version
    version = extract_section(issue_body, "### Version")
    if version:
        affected_label = "Affected/" + component + "-" + version
        if affected_label in all_existing_labels:
            labels.append(affected_label)

# Return verified labels
if len(labels) > 0:
    print(",".join(labels))
else:
    print("Missing/Component")
