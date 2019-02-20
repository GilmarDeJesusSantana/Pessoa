from django import forms

def adiciona_erro(self, message):
        self.full_clean()
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)