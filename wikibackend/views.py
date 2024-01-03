import markdown
from django.http import HttpResponse
from django.template import loader

from .models import Customer, WikiPage, WikiPage2Customer


def dashboard(request, customer_id):
    template = loader.get_template(
        "base.html"
    )

    template_opts = dict()

    template_opts["blogname"] = f"Wiki von {Customer.objects.get(pk=customer_id).name}"

    return HttpResponse(template.render(template_opts, request))


def wiki_page(request, customer_id, url):
    template = loader.get_template(
        "wiki_page.html"
    )

    template_opts = dict()

    template_opts["blogname"] = WikiPage.objects.get(url=url).name

    template_opts["pages"] = WikiPage2Customer.objects.filter(customer=customer_id)

    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])
    markdown_content = WikiPage.objects.get(url=url).content
    template_opts["content"] = md.convert(markdown_content)

    return HttpResponse(template.render(template_opts, request))
