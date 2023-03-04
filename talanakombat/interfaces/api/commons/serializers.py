from rest_framework import serializers


class ExceptionSerializer(serializers.Serializer):  # noqa
    code = serializers.ReadOnlyField(
        help_text="Unique error code. Doesn't contain whitespaces. Words are separated by underscores."
    )
    message = serializers.ReadOnlyField(help_text="Human-readable description of the error.")


class ResultSerializer(serializers.Serializer):  # noqa
    result = serializers.CharField(help_text="Descripción y respuesta de la pelea")
