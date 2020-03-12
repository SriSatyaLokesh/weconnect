from django.core.exceptions import ValidationError


def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("Content cannot be blank")
    abusive_words = ["fuck","fcuk","asshole","ass","poke","prick","bastard","arse","butt","porn","fecker","bitch","shit"]
    valid = True
    content = content.lower()
    for word in abusive_words:
        if word in content:
            valid = False
    if valid:
        return value
    else:
        raise ValidationError("Don't use abusive words")
