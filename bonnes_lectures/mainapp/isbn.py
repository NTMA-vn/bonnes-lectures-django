from django import forms
from django.core.exceptions import ValidationError


class Isbn:
    def __init__(self, value):
        if isinstance(value, Isbn):
            value = str(value)
        raw = str(value).strip()
        cleaned = raw.replace("-", "").replace(" ", "").upper()

        if len(cleaned) == 10:
            if not (cleaned[:9].isdigit() and (cleaned[9].isdigit() or cleaned[9] == "X")):
                raise ValidationError("Format ISBN-10 invalide.")
            self.prefix = None
            self.group = cleaned[0]
            self.publisher = cleaned[1:5]
            self.title = cleaned[5:9]
            self.check_digit = cleaned[9]
            self.digits = cleaned
        elif len(cleaned) == 13:
            if not cleaned.isdigit():
                raise ValidationError("Un ISBN-13 ne doit contenir que des chiffres.")
            if not cleaned.startswith(("978", "979")):
                raise ValidationError("Un ISBN-13 doit commencer par 978 ou 979.")
            self.prefix = cleaned[:3]
            self.group = cleaned[3]
            self.publisher = cleaned[4:8]
            self.title = cleaned[8:12]
            self.check_digit = cleaned[12]
            self.digits = cleaned
        else:
            raise ValidationError("Un ISBN doit comporter exactement 10 ou 13 caractères.")
        self.validate()

    def validate(self):
        """Validateur au sens de Django : lève ValidationError si la clé est fausse."""
        if len(self.digits) == 10:
            total = sum((10 - i) * int(ch) for i, ch in enumerate(self.digits[:9]))
            last = 10 if self.check_digit == "X" else int(self.check_digit)
            if (total + last) % 11 != 0:
                raise ValidationError("Clé de contrôle ISBN-10 invalide.")
        else:
            total = sum(
                int(ch) * (1 if i % 2 == 0 else 3)
                for i, ch in enumerate(self.digits[:12])
            )
            expected = (10 - (total % 10)) % 10
            if int(self.check_digit) != expected:
                raise ValidationError("Clé de contrôle ISBN-13 invalide.")

    def __str__(self):
        if self.prefix:
            return f"{self.prefix}-{self.group}-{self.publisher}-{self.title}-{self.check_digit}"
        return f"{self.group}-{self.publisher}-{self.title}-{self.check_digit}"

    def __int__(self):
        if self.digits.endswith("X"):
            return int(self.digits[:-1]) * 10 + 10
        return int(self.digits)

    def __eq__(self, other):
        if isinstance(other, Isbn):
            return self.digits == other.digits
        return False


class IsbnField(forms.CharField):

    def to_python(self, value):
        value = super().to_python(value)
        if not value:
            return None
        return Isbn(value)

    def validate(self, value):
        super().validate(value)
        if isinstance(value, Isbn):
            value.validate()