from books.models import Book, Edition, Text, Publisher, Person, Author
from django.contrib import admin

#class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'owner', 'edition')
    
#    def title(self, book):
#        return book.edition.text.title


#admin.site.register(Book, BookAdmin)
admin.site.register(Book)
admin.site.register(Edition)
admin.site.register(Text)
admin.site.register(Publisher)
admin.site.register(Person)
admin.site.register(Author)
