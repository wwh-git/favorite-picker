import re

def replace_content_with_names(names):
    # Read the content of picker.html
    with open('picker.html', 'r') as file:
        content = file.read()

    # Find the content between 'var items = [' and ']'
    pattern = re.compile(r'var items = \[([\s\S]*?)\];')
    match = pattern.search(content)

    if match:
        # Extract the content between 'var items = [' and ']'
        original_content = match.group(1)

        # Remove duplicates from the list of names and announce them
        unique_names = list(set(names))
        duplicates = set([name for name in names if names.count(name) > 1])

        if duplicates:
            print("Removed duplicate names:", ", ".join(duplicates))

        # Replace the content with unique names in the format "{id: 'Name'},"
        replaced_content = ',\n'.join(f"{{id: '{name}'}}" for name in unique_names)

        # Update the content in picker.html
        updated_content = content.replace(original_content, replaced_content)
        
        # Write the updated content back to picker.html
        with open('picker.html', 'w') as file:
            file.write(updated_content)

        print("Replacement completed successfully.")
    else:
        print("Could not find 'var items = [' and ']' in the file.")

# Get the list of names interactively from the user
names_input = input("Enter a line-separated list of names (press Enter twice to finish):\n")

# Continue to read lines until an empty line is encountered
names = []
while names_input.strip():
    names.append(names_input.strip())
    names_input = input()

# Call the function with the list of names
replace_content_with_names(names)
