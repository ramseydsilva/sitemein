from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from .models import SiteRequest


def home(request):
    email = ""
    if not request.user.is_anonymous():
        email = request.user.email
        user = request.user

    context = {"home_page": True, "email": email}
    return render_to_response("index.html", context, context_instance = RequestContext(request))

def features(request):
    context = {"features_page": True}
    return render_to_response("features.html", context, context_instance = RequestContext(request))

def price_list(request):
    context = {"price_list_page": True}
    return render_to_response("price_list.html", context, context_instance = RequestContext(request))

def about(request):
    context = {"about_page": True}
    return render_to_response("about.html", context, context_instance = RequestContext(request))

def work(request):
    sites = SiteRequest.objects.filter(published=True).order_by("-published_date")
    context = {"work_page": True, "sites": sites}
    return render_to_response("work.html", context, context_instance = RequestContext(request))

def create_site_success(request):
    context = {}
    return render_to_response("create_site_success.html", context, context_instance = RequestContext(request))

def create_site(request, errors={}):
    name = email = title = content = image_url = site_type = ""
    user = None

    if not request.user.is_anonymous():
        email = request.user.email
        user = request.user

    if request.POST:
        title = request.POST["title"]
        content = request.POST["content"]
        image_url = request.POST["image_url"]
        site_type = request.POST["site_type"]
        name = request.POST["name"]
        email = request.POST["email"]
        if title != "":
            site_request = SiteRequest(title=title, content=content, image_url=image_url, site_type=site_type,
                                        name=name, email=email, user=user)
            site_request.save()
            return redirect(reverse("create_site_success"))
        else:
            errors = {
                "title": "Please enter a title for your site",
            }

    context = {
        "title": title,
        "content": content,
        "image_url": image_url,
        "site_type": site_type,
        "name": name,
        "email": email,
        "errors": errors,
    }

    return render_to_response("index.html", context, context_instance = RequestContext(request))
