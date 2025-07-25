"""
Create a function that generates an invitation from a template for attendees

    Template (string)
    Attendees (list(dict))
    
    Returns: An output file replacing the placeholders in the template
"""

import os


def generate_invitations(template, attendees):
    """
        Confirms the template is a string
        Confirms the attendees is a list of dictionaries
    """
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list):
        for attendee in attendees:
            if not isinstance(attendees, dict):
                print("Error: Attendees should be a list of dictionaries.")
                return

    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            placeholder = "{" + key + "}"
            invitation = invitation.replace(placeholder, value)
        output_file = f"output_{index}.txt"

        if os.path.exists(output_file):
            print(f"Error: The file {output_file} already exists.")
            continue

        try:
            with open(output_file, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error: Impossible to write to the file {output_file}. Exception: {e}")
