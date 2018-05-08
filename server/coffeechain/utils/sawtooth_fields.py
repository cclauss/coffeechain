from rest_framework import fields


class KeyField(fields.SlugField):
    def __init__(self, **kwargs):
        kwargs.setdefault("required", True)
        kwargs.setdefault("min_length", 4)
        kwargs.setdefault("max_length", 32)
        super().__init__(**kwargs)


class NameField(fields.CharField):
    def __init__(self, **kwargs):
        kwargs.setdefault("min_length", 4)
        kwargs.setdefault("max_length", 128)
        super().__init__(**kwargs)
