import os
from django.shortcuts import render
from .functions import process_markdown_file
from .models import Customer


def wiki_page(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {"customer": customer}

    markdown_path = os.path.join("wikibackend", "markdown_files", "example.md")
    rendered_content = process_markdown_file(markdown_path, context)

    return render(request, "wiki_page.html", {"content": rendered_content})
