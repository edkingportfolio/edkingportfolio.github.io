# Load the HTML content for modifications

html_path = "nyu.html"



# Read the file content

with open(html_path, "r", encoding="utf-8") as file:

    html_content = file.read()



# Update content based on suggestions

updated_html_content = html_content.replace(

    "To obtain an MFA in Creative Writing at NYU.",

    "To further develop my craft as a writer and educator through the MFA in Creative Writing program at NYU, "

    "leveraging its distinguished faculty and vibrant creative community to complete my first novel and refine my teaching approach."

)



updated_html_content = updated_html_content.replace(

    "Created site to publish mine and others' stories.",

    "Founded an international storytelling platform, publishing over 100 stories from writers worldwide and showcasing diverse voices."

)



updated_html_content = updated_html_content.replace(

    "Designed and created site using WordPress, HTML, CSS, and PHP.",

    "Designed and managed the website using WordPress, HTML, CSS, and PHP."

)



# Replace relevant sections in "Work Experience"

updated_html_content = updated_html_content.replace(

    "<li>Taught English, Math, Engineering, AP Computer Science, and Creative Writing.</li>",

    "<li>Designed and taught a creative writing elective, guiding students in crafting short stories and personal essays while fostering their unique voices.</li>"

)



updated_html_content = updated_html_content.replace(

    "Worked in an classroom teaching English reading, writing, and speaking skills to primarily Somali refugees and immigrants.",

    "Taught English reading, writing, and speaking skills to Somali refugees, fostering cross-cultural communication and empathy."

)



# Save the modified HTML content

updated_html_path = "nyu_updated.html"

with open(updated_html_path, "w", encoding="utf-8") as updated_file:

    updated_file.write(updated_html_content)



updated_html_path
