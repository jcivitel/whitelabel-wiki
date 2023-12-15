import os
from markdown import markdown
from django.template import Template, Context


def process_markdown_file(file_path, context):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    template = Template(content)
    rendered_content = template.render(Context(context))

    return markdown(content)
