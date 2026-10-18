import math
from app.exceptions import ValidationError

"""Class that ensures that user inputs are valid."""
class InputValidator:
    
    """Validates calculator inputs."""

    @staticmethod
    def validate_number(value, config):
        try:
            number = float(value)

            if not math.isfinite(number):
                raise ValidationError("Input must be a finite number")

            if abs(number) > config.max_input_value:
                raise ValidationError(
                    f"Value exceeds maximum allowed: {config.max_input_value}"
                )

            return number

        except (ValueError, TypeError, OverflowError) as e:
            raise ValidationError(
                f"Invalid number format: {value}"
            ) from e