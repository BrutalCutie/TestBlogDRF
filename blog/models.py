from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=32,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"


class Article(models.Model):
    title = models.CharField(
        verbose_name="название",
        max_length=100,
    )
    text = models.TextField(
        verbose_name='текст статьи',
    )
    category = models.ForeignKey(
        "blog.Category",
        verbose_name="категория",
        on_delete=models.SET_NULL,
        related_name="articles",
        null=True,
        blank=False,
    )
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="автор статьи",
        related_name='articles',
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        verbose_name='время изменения',
        auto_now=True,
        null=True
    )

    def __str__(self):
        return f"{self.pk} | {self.author=}"

    def __repr__(self):
        return f"< {self.__class__.__name__} {self.__str__()}>"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Commentary(models.Model):
    article = models.ForeignKey(
        'blog.Article',
        on_delete=models.CASCADE,
        verbose_name='Статья',
    )

    text = models.TextField(
        verbose_name='текст комментария'
    )

    author = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='время создания',
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        verbose_name='время изменения',
        auto_now=True,
        null=True
    )

    def __str__(self):
        return f"{self.pk=} | {self.author=}"

    def __repr__(self):
        return f"< {self.__class__.__name__} {self.__str__()} >"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
