from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import LENGTH_STR

User = get_user_model()


class Group(models.Model):
    title = models.CharField('заголовок', max_length=200)
    slug = models.SlugField('слаг группы', unique=True)
    description = models.TextField('описание',)

    def __str__(self):
        return self.title[:LENGTH_STR]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор, на которого подписались'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

        def __str__(self):
            return (f'{self.user} является подписчиком {self.following}.')


class Post(models.Model):
    text = models.TextField('текст',)
    pub_date = models.DateTimeField(
        'дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор поста',
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='изображение к посту',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='группа поста',
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.text[:LENGTH_STR]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор комментария',

    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='пост комментария',
    )
    text = models.TextField('текст комментария',)
    created = models.DateTimeField(
        'дата добавления',
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return (f'Комментарий "{self.text[:LENGTH_STR]}" '
                f'автора "{self.author}" '
                f'к посту "{self.post}".')
