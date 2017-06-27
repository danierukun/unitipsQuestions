from django.db import models

# Crea tus modelos de preguntas y respuestas para el quiz aquí.

class Question(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

    def __str__(self):
        return self.text
