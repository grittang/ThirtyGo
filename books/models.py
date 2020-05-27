from django.db import models

# Create your models here.
class Book(models.Model):
    """A book the user is reading or translating."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=60)
    link = models.URLField(unique=True, blank=True)
    pub_year = models.CharField(max_length=4, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # date_updated = models.DateTimeField('Last Updated')

    def __str__(self):
        return f"{self.title} by {self.author}"

class Review(models.Model):
    """A piece of review given on a book."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    reviewer = models.CharField(max_length=60, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'reviews'

    def __str__(self):
        max_len = 200
        if len(self.text) > max_len:
            return f"{self.text[:max_len]}..."
        else:
            return f"{self.text}"

class Source(models.Model):
    """Some sentences extracted from a book."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    original_sentence = models.TextField(max_length=1000)
    recommended_trans = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'sources'

    def __str__(self):
        return self.original_sentence

class Translation(models.Model):
    """A translation given on the sentences."""
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=1000)
    translator = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'translations'

    def __str__(self):
        return f"{self.translator}: {self.text}"
