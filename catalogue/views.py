from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PageForm
from .models import Category, Page


def page_list(request, category_slug=None):
    category = None
    search_query = request.GET.get("search", "")
    categories = Category.objects.all()
    pages = Page.objects.all()
    if search_query and not category_slug:
        pages = Page.objects.filter(
            Q(name__icontains=search_query) | Q(description__icontains=search_query)
        )
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        pages = pages.filter(category=category)

    paginator = Paginator(pages, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    next_url = ""
    prev_url = ""

    if page_obj.has_next():
        next_url = f"?page={page_obj.next_page_number()}"

    if page_obj.has_previous():
        prev_url = f"?page={page_obj.previous_page_number()}"

    return render(
        request,
        "catalogue/list.html",
        {
            "category": category,
            "categories": categories,
            "pages": page_obj,
            "previous_page_url": prev_url,
            "next_page_url": next_url,
        },
    )


def list_new(request):
    if request.method == "POST":
        form = PageForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print("validation here")
            post = form.save(commit=False)
            post.save()
            request.session["post_id"] = post.id
            return redirect("thanks/")
    form = PageForm()
    return render(request, "catalogue/newlisting.html", {"form": form})


def thank_you(request):
    for key, value in request.session.items():
        print("{} => {}".format(key, value))
    if "post_id" not in request.session:
        return HttpResponseForbidden()
    return render(request, "catalogue/thankyou.html")


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request,
#                   'shop/product/detail.html',
#                   {'product': product,
#                    'cart_product_form': cart_product_form})
