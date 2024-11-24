# import re
#
#
# def validate_and_extract_dates(text):
#     # Define regex patterns for each date format
#     patterns = [
#         r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b',  # DD/MM/YYYY
#         r'\b(0[1-9]|1[0-9]|2[0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})\b',  # MM-DD-YYYY
#         r'\b(\d{4})\.(0[1-9]|1[0-2])\.(0[1-9]|[12][0-9]|3[01])\b'  # YYYY.MM.DD
#     ]
#
#     valid_dates = []
#
#     for pattern in patterns:
#         matches = re.findall(pattern, text)
#         for match in matches:
#             # Join tuple elements to form the date string
#             if isinstance(match, tuple):
#                 date_str = '/'.join(match) if pattern == patterns[0] else '-'.join(match) if pattern == patterns[
#                     1] else '.'.join(match)
#             else:
#                 date_str = match
#
#             valid_dates.append(date_str)
#
#     return valid_dates
#

# Example usage:
# text = "The event is on 23/05/2023 and the follow-up is on 2023.06.15. Don't forget the deadline on 09-12-2023."
# extracted_dates = validate_and_extract_dates(text)
# print(extracted_dates)
#
#
# ['23/05/2023', '2023.06.15', '09-12-2023']
#


import re
from datetime import datetime


def validate_and_extract_dates(texts):
    # Regular expression for matching the three date formats
    date_pattern = r'(\b\d{2}/\d{2}/\d{4}\b)|(\b\d{2}-\d{2}-\d{4}\b)|(\b\d{4}\.\d{2}\.\d{2}\b)'

    # Find all matches for the date pattern
    potential_dates = re.findall(date_pattern, text)

    # Flatten the result since findall gives tuples
    potential_dates = [date for tup in potential_dates for date in tup if date]

    valid_dates = []

    # Iterate through each potential date and validate
    for date_str in potential_dates:
        try:
            # Check the format and parse the date accordingly
            if '/' in date_str:
                parsed_date = datetime.strptime(date_str, '%d/%m/%Y')
            elif '-' in date_str:
                parsed_date = datetime.strptime(date_str, '%m-%d-%Y')
            elif '.' in date_str:
                parsed_date = datetime.strptime(date_str, '%Y.%m.%d')

            # Append valid dates to the list
            valid_dates.append(date_str)
        except ValueError:
            # Invalid date will raise a ValueError, so we skip it
            continue

    return valid_dates


# Example usage
with open("Hw11.2.txt", 'r') as file:
    text = file.read()

print(validate_and_extract_dates(text))


