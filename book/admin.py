from django.contrib import admin
from .models import Book
import csv
from django.http import HttpResponse


# Add new actions
@admin.action(description='Activate selected items')
def activate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Deactivate selected items')
def deactivate_selected_items(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description='Download selected items as csv')
def download_csv(self, request, queryset):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books.csv"'
        writer = csv.writer(response)
        writer.writerow([
             'id',
             'title',
             'writer',
             'rating',
             'number_of_editions',
             'is_active',
             'created_date',
             'updated_date'
        ])
        data = Book.objects.filter()
        for row in data:
            rowobj = [
                 row.id,
                 row.title,
                 row.writer,
                 row.rating,
                 row.number_of_editions,
                 row.is_active,
                 row.created_date,
                 row.updated_date,
            ]
            
            writer.writerow(rowobj)

        return response


@admin.register(Book)
class AdminCategory(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'writer',
        'rating',
        'number_of_editions',
        'is_active',
        'created_date',
        'updated_date',
    )
    list_display_links = ('id', 'title',)
    list_filter = ('is_active', 'created_date', 'updated_date',)
    list_editable = ('is_active',)
    # Order by primary key
    ordering = ('pk',)

    actions = (
        activate_selected_items,
        deactivate_selected_items,
        download_csv,
    )
