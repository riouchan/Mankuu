from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import ManqooRelations
from .forms import ManqooRelationsForm
from django.core.paginator import Paginator
from django.db.models import Q


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to your app's main page after login
            return redirect('mankuu_homepage')
        else:
            # Add error message
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')  # Render the login template


@login_required
def mankuu_hompepage(request):
    return render(request, 'homepage.html')


@login_required
def manqoo_relations_view(request):
    # Define all sortable fields
    sortable_fields = [
        'customer_code', 'parking_name', 'start_rack', 'end_rack',
        'machine_id', 'area_code', 'id'  # Add fields here as needed
    ]

    # Get the ordering field from the request (defaulting to 'id')
    ordering = request.GET.get('ordering', 'id')

    # Validate if the ordering field is in sortable_fields
    if ordering.lstrip('-') not in sortable_fields:
        ordering = 'id'  # Fallback to a default ordering

    # Set the ordering direction for toggling
    new_ordering = f'-{ordering.lstrip("-")}' if not ordering.startswith(
        '-') else ordering.lstrip('-')

    # Get the search query from the request
    search_query = request.GET.get('search', '')

    # Retrieve the queryset, filtered by search if applicable
    manqoo_relations = ManqooRelations.objects.all()

    if search_query:
        # Use Q objects to filter by multiple fields
        manqoo_relations = manqoo_relations.filter(
            Q(customer_code__icontains=search_query) |
            Q(parking_name__icontains=search_query) |
            Q(start_rack__icontains=search_query) |
            Q(end_rack__icontains=search_query) |
            Q(machine_id__icontains=search_query) |
            Q(area_code__icontains=search_query)
        )

    # Apply ordering
    manqoo_relations = manqoo_relations.order_by(ordering)

    # Set pagination size, defaulting to 10
    page_size = int(request.GET.get('page_size', 10))
    paginator = Paginator(manqoo_relations, page_size)

    # Get current page number and total pages
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number  # Current page number
    page_now = int(request.GET.get('page_size', 10))

    # Pass the page_obj, ordering, new_ordering, search_query, current_page, and total_pages to the template
    return render(request, 'index.html', {
        'page_obj': page_obj,
        'ordering': ordering,
        'page_now': page_now,
        'new_ordering': new_ordering,
        'page_size': page_size,
        'search_query': search_query,
        'current_page': current_page,

    })


@login_required
def create_mankuu_info(request):
    manqoo_relations = ManqooRelations.objects.all()
    if request.method == 'POST':
        form = ManqooRelationsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            # Add a success message
            messages.success(
                request, f"新規駐輪所 ({instance.parking_name}) 作成完了しました。")
            return redirect('mankuu_detail')
    else:
        form = ManqooRelationsForm()

    return render(request, 'create_mankuu.html', {'form': form})


@login_required
def edit_mankuu(request, pk):
    # Fetch the object by primary key (pk)
    mankuu = ManqooRelations.objects.get(id=pk)
    form = ManqooRelationsForm(instance=mankuu)
    if request.method == 'POST':
        form = ManqooRelationsForm(request.POST, instance=mankuu)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"駐輪所「{mankuu.parking_name}」の編集が完了しました。")
            return redirect('mankuu_detail')  # Redirect to a suitable page
    context = {
        'form': form,
        'mankuu': mankuu,  # Add `mankuu` to the context
    }
    return render(request, 'edit_mankuu.html', context)


@login_required
def delete_mankuu(request, pk):
    mankuu = ManqooRelations.objects.get(id=pk)
    parking_name = mankuu.parking_name
    if request.method == 'POST':
        mankuu.delete()
        messages.success(request, f"駐輪場名「{parking_name}」が削除されました。")
        return redirect('mankuu_detail')  # Redirect after successful deletion
    context = {'mankuu': mankuu}
    return render(request, 'confirm_delete.html', context)


def logoutUser(request):
    logout(request)
    return redirect("login")
