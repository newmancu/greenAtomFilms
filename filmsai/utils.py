
from filmsai import models

def predict(comment_id: int) -> None:
    """
    Функция для вызова моделей
    """
    # comment - объект комментрания в базе данных, который будет изменен
    comment = models.Comment.objects.get(id=comment_id)

    # Код для обновления полей коментария
    import random
    comment.rating = random.randint(0,10)
    comment.assesment = random.random() > .5
    comment.save()
    pass