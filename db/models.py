from django.db.models import Model, TextField, DateTimeField, PositiveIntegerField, FloatField, OneToOneField, CASCADE


class Face(Model):
    id = PositiveIntegerField(primary_key=True)  # Map with face_id from person
    confidence = FloatField()
    x = FloatField()
    y = FloatField()
    width = FloatField()
    height = FloatField()
    image_path = TextField()
    datetime = DateTimeField()


class Person(Model):
    name = TextField()
    face_id = OneToOneField(Face, on_delete=CASCADE, )
