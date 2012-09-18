from django import forms
from books.models import Person, BookCollection, Book, Edition, Text, Location

class EditionForm(forms.ModelForm):
    class Meta:
        model = Edition

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
    def __init__(self, post, instance):
        self.edition_form = EditionForm(instance=instance.edition)
        self.text_form = TextForm(instance=instance.edition.text)
        super(BookForm, self).__init__(instance=instance)

