import markdown
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from .forms import EditorForm
from .models import Customer, WikiPage, WikiPage2Customer


def dashboard(request, customer_id):
    template = loader.get_template(
        "dashboard.html"
    )

    template_opts = dict()

    template_opts["customer"] = Customer.objects.get(pk=customer_id)

    template_opts["blogname"] = f"{Customer.objects.get(pk=customer_id).name}"

    template_opts["pages"] = WikiPage2Customer.objects.filter(customer=customer_id)

    return HttpResponse(template.render(template_opts, request))


def wiki_page(request, customer_id, url):
    template = loader.get_template(
        "wiki_page.html"
    )

    template_opts = dict()

    template_opts["customer"] = Customer.objects.get(pk=customer_id)

    template_opts["blogname"] = f"{Customer.objects.get(pk=customer_id).name}"

    template_opts["pages"] = WikiPage2Customer.objects.filter(customer=customer_id)

    md = markdown.Markdown(extensions=["fenced_code", "codehilite"])
    markdown_content = WikiPage.objects.get(url=url).content
    template_opts["content"] = md.convert(markdown_content)

    return HttpResponse(template.render(template_opts, request))


@login_required
def upload_image(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)

    if request.method == "POST":
        return redirect(f"/wiki/{customer.id}")
    else:
        return redirect(f"/wiki/{customer.id}")


@login_required
def edit_page(request, customer_id, url):
    template = loader.get_template("edit_page.html")

    template_opts = dict()

    template_opts["customer"] = Customer.objects.get(pk=customer_id)

    template_opts["blogname"] = f"{Customer.objects.get(pk=customer_id).name}"

    template_opts["pages"] = WikiPage2Customer.objects.filter(customer=customer_id)

    if request.method == "POST":
        edit_form = EditorForm(request.POST)
        if edit_form.is_valid():
            pass

    else:
        edit_form = EditorForm(instance=WikiPage.objects.get(url=url))

    template_opts["edit_form"] = edit_form

    return HttpResponse(template.render(template_opts, request))
