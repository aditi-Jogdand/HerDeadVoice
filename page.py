import os
import markdown

# Directory containing Markdown files
md_dir = 'C:/Users/akrat/Downloads/HerDeadVoiceWs'
# Directory to save the HTML files
html_dir = 'C:/Users/akrat/Downloads/HerDeadVoiceWs'

# Ensure the html directory exists
os.makedirs(html_dir, exist_ok=True)

# Function to convert Markdown to HTML
def convert_md_to_html(md_content):
    html_content = markdown.markdown(md_content, extensions=['nl2br'])
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Poem</title>
    <link rel="stylesheet" href="./page.css">
    <link rel="stylesheet" href="../herdeadvoice/assets/css/style2.css">
</head>
<body>
    <div class="background"></div>
    <div class="woolf"></div>
    <div class="content-container">
        <div class="content">
            {html_content}
        </div>
    </div>
</body>
</html>
"""

# Iterate through Markdown files and convert them
for filename in os.listdir(md_dir):
    if filename.endswith('.md'):
        with open(os.path.join(md_dir, filename), 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        html_content = convert_md_to_html(md_content)
        
        # Save the HTML content to a new file
        html_filename = os.path.splitext(filename)[0] + '.html'
        with open(os.path.join(html_dir, html_filename), 'w', encoding='utf-8') as f:
            f.write(html_content)

print("Conversion complete!")
