# JiraQuest 🌌

Embark on a journey to uncover insights from your Jira comments.

JiraQuest is an open-source project designed to help teams process and analyze Jira comments efficiently. With built-in integrations for Tableau and Slack, along with a powerful CLI, JiraQuest empowers teams to focus on actionable insights, visualize trends, and stay connected.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jiraquest)
![PyPI version](https://img.shields.io/pypi/v/jiraquest)
![License](https://img.shields.io/github/license/rainbowgore/JiraQuest)

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Setup](#setup)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Tableau Integration](#tableau-integration)
  - [Slack Integration](#slack-integration)
- [Example Files](#example-files)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

JiraQuest simplifies Jira comment analysis by automating the process of fetching, filtering, and formatting comments. It is highly customizable and suitable for various teams, including developers, Atlassian admins, quality assurance, project management, and more. Whether you want detailed reports, visual insights, or Slack updates, JiraQuest has you covered.

---

## Features

- **Automated Comment Processing**: Fetch and filter comments from Jira issues with ease.
- **Customizable Exclusions**: Exclude specific users or teams from reports.
- **Tableau Integration**: Export data to a SQLite database for powerful visualizations.
- **Slack Integration**: Send summarized reports directly to Slack channels.
- **Sentiment Analysis** *(optional)*: Gain insights into the sentiment of comments.
- **Flexible CLI**: Run all operations from the command line.

---

## Installation

JiraQuest is available on PyPI. You can install it using pip:

```bash
pip install jiraquest
```

Alternatively, you can clone the repository and install the dependencies manually:

```bash
git clone https://github.com/rainbowgore/JiraQuest.git
cd jiraquest
pip install -r requirements.txt
```

---

## Quick Start

1. Install JiraQuest:
   ```bash
   pip install jiraquest
   ```

2. Set up your `.env` file:
   ```plaintext
   JIRA_URL=https://your-jira-instance.atlassian.net
   USERNAME=your-email@example.com
   TOKEN=your-api-token
   ```

3. Run the CLI:
   ```bash
   jiraquest --generate-report
   ```

---

## Setup

1. Create a `.env` file in the root directory with the following environment variables:

   ```plaintext
   # Jira Configuration
   JIRA_URL=https://your-jira-instance.atlassian.net
   USERNAME=your-email@example.com
   TOKEN=your-api-token

   # File Paths
   INPUT_FILE=data/input_file.xlsx
   NEW_OUTPUT_JSON=data/formatted_last_3_comments.json
   REPORT_FILE=data/final_report.csv
   DB_FILE=data/jira_comments.db

   # Slack Integration
   SLACK_WEBHOOK_URL=https://hooks.slack.com/services/your/slack/webhook
   ```

2. Prepare your input Excel file (`input_file.xlsx`) with the following structure:

   | Key      | Components |
   | -------- | ---------- |
   | PROJ-123 | Frontend   |
   | PROJ-124 | Backend    |

3. Add a file `excluded_users.txt` (optional) to define users to exclude from reports:

   ```plaintext
   John Doe
   Jane Smith
   ```

---

## Usage

### Command-Line Interface (CLI)

Run the script with the following commands:

1. **Generate Reports**:
   ```bash
   jiraquest --generate-report
   ```

   Output:
   - JSON: `formatted_last_3_comments.json`
   - CSV: `final_report.csv`

2. **Save to Database**:
   ```bash
   jiraquest --save-to-database
   ```

   Output:
   - SQLite Database: `jira_comments.db`

3. **Send Report to Slack**:
   ```bash
   jiraquest --slack-me
   ```

   Example Slack message:
   ```plaintext
   🔔 JiraQuest Alert 🚀 New Insights from Jira Comments:
   Issue Key: PROJ-123
   Component: Frontend
   Latest Comment: "The feature is not working as expected."
   Author: John Doe
   Timestamp: 2025-01-10 12:34:56
   ```

4. **Combine Actions**:
   ```bash
   jiraquest --generate-report --save-to-database --slack-me
   ```

### Tableau Integration

After running the `--save-to-database` command, connect Tableau to the SQLite database:

1. Open Tableau.
2. Connect to the database file (`jira_comments.db`).
3. Visualize the data using Tableau's drag-and-drop interface.

### Slack Integration

Ensure your Slack webhook URL is set in the `.env` file. Run the following command to send reports:

```bash
jiraquest --slack-me
```

---

## Example Files

You'll find the following example files in the `data` directory:

1. **`sample_input.xlsx`**: A template for input data with example Jira issue keys and components.

2. **`excluded_users.txt`**: A template for excluded users.

---

## Example Output

### JSON File (`formatted_last_3_comments.json`):

```json
[
    {
        "Instance": "https://your-jira-instance.atlassian.net",
        "Issue Key": "PROJ-123",
        "Component": "Frontend",
        "Comment-1": "The feature is not working as expected.",
        "Author-1": "John Doe",
        "Email-1": "john@example.com",
        "Created-1": "2025-01-10T12:34:56Z",
        "Comment-2": "I have fixed the issue.",
        "Author-2": "Jane Smith",
        "Email-2": "jane@example.com",
        "Created-2": "2025-01-11T08:22:33Z",
        "Comment-3": "The fix has been deployed.",
        "Author-3": "John Doe",
        "Email-3": "john@example.com",
        "Created-3": "2025-01-12T09:45:12Z"
    }
]
```

---

## Contributing

Contributions are welcome! Here’s how you can get involved:

1. **Fork the Repository**: Click on the "Fork" button at the top-right corner of this page.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/yourusername/jiraquest.git
   cd jiraquest
   ```
3. **Install Development Dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```
4. **Make Changes**: Add your feature or fix bugs.
5. **Run Tests**:
   ```bash
   pytest
   ```
6. **Submit a Pull Request**: Push your changes and open a pull request.

For more details, check our [Contributing Guidelines](CONTRIBUTING.md).

---

## License

The project is available as open source under the terms of the MIT License.

