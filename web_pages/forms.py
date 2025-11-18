from datetime import datetime

from django.forms import forms, ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "published_date",
            "cover"
        ]

    # title length constraint
    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters")

        return title

    # published_date range constraint
    def clean_published_date(self):
        published_date = self.cleaned_data["published_date"]
        published_datetime = datetime(published_date.year, published_date.month, published_date.day)

        current_datetime = datetime.now()

        if published_datetime > current_datetime:
            raise forms.ValidationError("Published date cannot be in the future")

        return published_date

    # cross-field validation of title and author
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        author = cleaned_data.get("author")

        if "draft" in title and author == "Unknown":
            raise forms.ValidationError("Author cannot be 'Unknown' if Title is 'draft'")

        return cleaned_data

