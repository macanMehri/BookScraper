from django.db import models


class BaseModel(models.Model):

    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active'
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created Date'
    )

    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated Date'
    )


    class Meta:
        abstract = True


    def __str__(self) -> str:
        raise NotImplementedError('You did not override the string method!')


class Book(BaseModel):

    title = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Book Title'
    )

    writer = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Book Writer'
    )

    rating = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Book Rate'
    )

    published_year = models.IntegerField(verbos_name='Published Year')

    number_of_editions = models.IntegerField(verbos_name='Number Of Editions')
