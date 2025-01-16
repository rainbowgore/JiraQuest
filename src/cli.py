import argparse
import os
from jira_comments_script import process_workflow
from tableau_integration import save_to_database
from slack_integration import send_report_to_slack
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment Variables
INPUT_FILE = os.getenv("INPUT_FILE", "data/input_file.xlsx")
NEW_OUTPUT_JSON = os.getenv("NEW_OUTPUT_JSON", "data/formatted_last_3_comments.json")
REPORT_FILE = os.getenv("REPORT_FILE", "data/final_report.csv")
DB_FILE = os.getenv("DB_FILE", "data/jira_comments.db")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")


def main():
    """
    Main function for the JiraQuest CLI.
    Parses command-line arguments and triggers the corresponding functionality.
    """
    parser = argparse.ArgumentParser(description="JiraQuest CLI - Analyze and manage Jira comments.")

    # Define CLI arguments
    parser.add_argument(
        "--generate-report",
        action="store_true",
        help="Generate JSON and CSV reports from Jira comments."
    )
    parser.add_argument(
        "--save-to-database",
        action="store_true",
        help="Save the generated CSV report to the SQLite database for Tableau integration."
    )
    parser.add_argument(
        "--slack-me",
        action="store_true",
        help="Send the summarized report to a Slack channel."
    )

    args = parser.parse_args()

    # Handle each argument
    if args.generate_report:
        print("Generating reports...")
        process_workflow(INPUT_FILE, NEW_OUTPUT_JSON, REPORT_FILE)

    if args.save_to_database:
        if not os.path.exists(REPORT_FILE):
            print(f"Error: Report file '{REPORT_FILE}' does not exist. Generate the report first.")
        else:
            print("Saving report to database...")
            save_to_database(REPORT_FILE, DB_FILE)

    if args.slack_me:
        if not SLACK_WEBHOOK_URL:
            print("Error: Slack webhook URL is not configured. Set the SLACK_WEBHOOK_URL environment variable.")
        else:
            print("Sending report to Slack...")
            send_report_to_slack(SLACK_WEBHOOK_URL, NEW_OUTPUT_JSON)

    # If no arguments provided, display a message
    if not any(vars(args).values()):
        parser.print_help()


if __name__ == "__main__":
    main()