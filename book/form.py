from django import forms
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'genre',
                  'isbn', 'publication_date']

        widgets = {
            'title' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Title'
            }),
            'author' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Author Name'
            }),
            'description' : forms.Textarea(attrs={
                'class': 'form-control',
                'row': 4,
                'placeholder': 'Enter Book Description'
            }),
            'genre' : forms.Select(attrs={
                'class': 'form-control',
            }),
            'isbn' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN'
            }),
            'publication_date' : forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

        }