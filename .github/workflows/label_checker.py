import os
import requests
import sys

# Get all existing labels in the repository
labels = []
all_existing_labels = []
response = requests.get('https://api.github.com/repos/wso2/api-manager/labels', headers={"Accept": "application/vnd.github.v3+json"})
if response.status_code == 200:
    for label in response.json():
        all_existing_labels.append(label["name"])
else:
    exit(0)

try:
    # Check if ISSUE_BODY environment variable exists
    issue_body = os.environ.get("ISSUE_BODY", "")
    if not issue_body:
        print("Missing/Component")
        sys.exit(0)
    
    # Get affected component
    if "### Affected Component" not in issue_body or "### Version" not in issue_body:
        print("Missing/Component")
        sys.exit(0)
    
    i = issue_body.index("### Affected Component")
    j = issue_body.index("### Version")
    component = issue_body[i+25:j].strip()
    component_label = "Component/" + component
    if component_label in all_existing_labels:
        labels.append(component_label)
    
    # Get component version - extract until next newline or end of string
    version_start = j + 13
    version_text = issue_body[version_start:].strip()
    # Extract version until newline or '###' (next section)
    version_end = len(version_text)
    for idx, char in enumerate(version_text):
        if char in ['\n', '\r'] or version_text[idx:idx+3] == '###':
            version_end = idx
            break
    version = version_text[:version_end].strip()
    
    if version:
        affected_label = "Affected/" + component + "-" + version
        if affected_label in all_existing_labels:
            labels.append(affected_label)
    
    # Return verified labels
    if len(labels) > 0:
        print(",".join(labels))
    else:
        print("Missing/Component")
        
except Exception as e:
    # If any error occurs, default to Missing/Component label
    print("Missing/Component")
    sys.exit(0)
