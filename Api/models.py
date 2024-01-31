from django.db import models
from uuid import uuid4

class User(models.Model):
    userID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField("Nome", max_length=255, null=False, blank=False)
    profileName = models.CharField("Nome do perfil", max_length=255, null=False, blank=False)
    date_of_birth = models.DateField("Data de nascimento", null=False, blank=False)
    email = models.EmailField("Email", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self) -> str:
        return self.name
    
class Discussions(models.Model):
    postID = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    linkPost = models.CharField("Link pessoal", max_length=255, null=False, blank=False)
    date = models.DateTimeField("Data da publicação", auto_now_add=True, null=False, blank=False)
    title = models.CharField("Título", max_length=255, null=False, blank=False)
    description = models.TextField("Descrição", null=False, blank=False)
    image = models.FileField("Imagem do post", upload_to="imagens", null=False, blank=False)
    likes = models.IntegerField("Likes na publicação")
    reads = models.IntegerField("Leituras na publicação")

    class Meta:
        verbose_name = 'Discussão'
        verbose_name_plural = 'Discussões'

    def __str__(self) -> str:
        return "{} - Publicado em {}".format(self.user.name, self.date)