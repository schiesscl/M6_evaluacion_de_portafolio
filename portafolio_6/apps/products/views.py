from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm, CategoryForm

# ========== VISTAS DE PRODUCTOS ==========

def product_list(request):
    """Vista de listado de productos con búsqueda y filtrado"""
    products = Product.objects.filter(is_active=True)
    
    # Búsqueda
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Filtro por categoría
    category_id = request.GET.get('category', '')
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Paginación
    paginator = Paginator(products, 9)  # 9 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    """Vista de detalle de un producto"""
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(pk=pk)[:4]
    
    context = {
        'product': product,
        'related_products': related_products
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def product_create(request):
    """Vista para crear un nuevo producto"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request, f'Producto "{product.name}" creado exitosamente.')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'title': 'Crear Producto',
        'button_text': 'Crear Producto'
    })

@login_required
def product_edit(request, pk):
    """Vista para editar un producto existente"""
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto "{product.name}" actualizado exitosamente.')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {
        'form': form,
        'product': product,
        'title': 'Editar Producto',
        'button_text': 'Guardar Cambios'
    })

@login_required
def product_delete(request, pk):
    """Vista para eliminar un producto"""
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'Producto "{product_name}" eliminado exitosamente.')
        return redirect('products:product_list')
    
    return render(request, 'products/product_confirm_delete.html', {
        'product': product
    })

# ========== VISTAS DE CATEGORÍAS ==========

@login_required
def category_list(request):
    """Vista de listado de categorías"""
    categories = Category.objects.all()
    
    context = {
        'categories': categories
    }
    return render(request, 'products/category_list.html', context)

@login_required
def category_create(request):
    """Vista para crear una nueva categoría"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Categoría "{category.name}" creada exitosamente.')
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    
    return render(request, 'products/category_form.html', {
        'form': form,
        'title': 'Crear Categoría',
        'button_text': 'Crear Categoría'
    })

@login_required
def category_edit(request, pk):
    """Vista para editar una categoría existente"""
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Categoría "{category.name}" actualizada exitosamente.')
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'products/category_form.html', {
        'form': form,
        'category': category,
        'title': 'Editar Categoría',
        'button_text': 'Guardar Cambios'
    })

@login_required
def category_delete(request, pk):
    """Vista para eliminar una categoría"""
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        category_name = category.name
        category.delete()
        messages.success(request, f'Categoría "{category_name}" eliminada exitosamente.')
        return redirect('products:category_list')
    
    return render(request, 'products/category_confirm_delete.html', {
        'category': category
    })
