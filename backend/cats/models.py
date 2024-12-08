from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Achievement(models.Model):
    name = models.CharField('Умелки шерстяного', max_length=64)

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name


class Cat(models.Model):
    name = models.CharField('Погоняло', max_length=16)
    color = models.CharField('Масть', max_length=16)
    birth_year = models.IntegerField('Дата появления на свет божий')
    owner = models.ForeignKey(
        User, related_name='cats',
        verbose_name='Хозяин',
        on_delete=models.CASCADE
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat'
    )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='cats/images/',
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Котик'
        verbose_name_plural = 'Котики'

    def __str__(self):
        return self.name


class AchievementCat(models.Model):
    achievement = models.ForeignKey(
        Achievement,
        verbose_name='Достижение',
        on_delete=models.CASCADE
    )
    cat = models.ForeignKey(
        Cat,
        verbose_name='Котик',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return f'{self.achievement} {self.cat}'
