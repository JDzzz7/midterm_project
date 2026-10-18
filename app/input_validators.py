from app.exceptions import ValidationError

"""Class for validating calculator inputs."""
class InputValidator:
    """Validates calculator inputs."""

    @staticmethod
    def validate_number(value, config):
        try:
            number = float(value)

            if abs(number) > config.max_input_value:
                raise ValidationError(
                    f"Value exceeds maximum allowed: {config.max_input_value}"
                )

            return number

        except (ValueError, TypeError) as e:
            raise ValidationError(
                f"Invalid number format: {value}"
            ) from e