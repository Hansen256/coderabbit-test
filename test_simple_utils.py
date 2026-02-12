"""
Unit tests for simple_utils.py

Tests cover main functionality and edge cases for:
- reverse_string
- count_words
- celsius_to_fahrenheit
"""

import pytest
from simple_utils import reverse_string, count_words, celsius_to_fahrenheit


class TestReverseString:
    """Test suite for reverse_string function."""

    def test_reverse_normal_string(self):
        """Test reversing a normal string."""
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        assert reverse_string("") == ""

    def test_reverse_single_character(self):
        """Test reversing a single character."""
        assert reverse_string("a") == "a"

    def test_reverse_palindrome(self):
        """Test reversing a palindrome."""
        assert reverse_string("racecar") == "racecar"

    def test_reverse_with_spaces(self):
        """Test reversing a string with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_with_numbers(self):
        """Test reversing a string with numbers."""
        assert reverse_string("abc123") == "321cba"

    def test_reverse_with_special_characters(self):
        """Test reversing a string with special characters."""
        assert reverse_string("!@#$%") == "%$#@!"

    def test_reverse_unicode(self):
        """Test reversing a string with unicode characters."""
        assert reverse_string("hello🌍") == "🌍olleh"

    def test_reverse_multiline_string(self):
        """Test reversing a multiline string."""
        assert reverse_string("line1\nline2") == "2enil\n1enil"


class TestCountWords:
    """Test suite for count_words function."""

    def test_count_single_word(self):
        """Test counting a single word."""
        assert count_words("hello") == 1

    def test_count_multiple_words(self):
        """Test counting multiple words."""
        assert count_words("hello world") == 2

    def test_count_empty_string(self):
        """Test counting words in an empty string."""
        assert count_words("") == 0

    def test_count_with_multiple_spaces(self):
        """Test counting words with multiple spaces between them."""
        assert count_words("hello  world") == 2

    def test_count_with_leading_spaces(self):
        """Test counting words with leading spaces."""
        assert count_words("  hello world") == 2

    def test_count_with_trailing_spaces(self):
        """Test counting words with trailing spaces."""
        assert count_words("hello world  ") == 2

    def test_count_with_tabs(self):
        """Test counting words separated by tabs."""
        assert count_words("hello\tworld") == 2

    def test_count_with_newlines(self):
        """Test counting words separated by newlines."""
        assert count_words("hello\nworld") == 2

    def test_count_only_whitespace(self):
        """Test counting words in a string with only whitespace."""
        assert count_words("   ") == 0

    def test_count_sentence(self):
        """Test counting words in a full sentence."""
        assert count_words("The quick brown fox jumps") == 5

    def test_count_with_punctuation(self):
        """Test counting words with punctuation (punctuation stays with words)."""
        assert count_words("Hello, world!") == 2


class TestCelsiusToFahrenheit:
    """Test suite for celsius_to_fahrenheit function."""

    def test_freezing_point(self):
        """Test converting water freezing point (0°C)."""
        assert celsius_to_fahrenheit(0) == 32.0

    def test_boiling_point(self):
        """Test converting water boiling point (100°C)."""
        assert celsius_to_fahrenheit(100) == 212.0

    def test_negative_temperature(self):
        """Test converting negative temperature."""
        assert celsius_to_fahrenheit(-40) == -40.0

    def test_positive_temperature(self):
        """Test converting a positive temperature."""
        result = celsius_to_fahrenheit(25)
        assert result == pytest.approx(77.0, rel=1e-9)

    def test_absolute_zero(self):
        """Test converting absolute zero (-273.15°C)."""
        result = celsius_to_fahrenheit(-273.15)
        assert result == pytest.approx(-459.67, rel=1e-9)

    def test_body_temperature(self):
        """Test converting normal body temperature (37°C)."""
        result = celsius_to_fahrenheit(37)
        assert result == pytest.approx(98.6, rel=1e-9)

    def test_decimal_temperature(self):
        """Test converting a temperature with decimals."""
        result = celsius_to_fahrenheit(20.5)
        assert result == pytest.approx(68.9, rel=1e-9)

    def test_high_temperature(self):
        """Test converting a very high temperature."""
        result = celsius_to_fahrenheit(1000)
        assert result == pytest.approx(1832.0, rel=1e-9)

    def test_zero_kelvin_boundary(self):
        """Test converting temperature near absolute zero."""
        result = celsius_to_fahrenheit(-273)
        assert result == pytest.approx(-459.4, rel=1e-9)

    def test_room_temperature(self):
        """Test converting room temperature (20°C)."""
        result = celsius_to_fahrenheit(20)
        assert result == pytest.approx(68.0, rel=1e-9)


# Additional regression and boundary tests
class TestEdgeCasesAndRegressions:
    """Additional tests for edge cases and potential regressions."""

    def test_reverse_string_preserves_type(self):
        """Ensure reverse_string returns a string type."""
        result = reverse_string("test")
        assert isinstance(result, str)

    def test_count_words_returns_int(self):
        """Ensure count_words returns an integer."""
        result = count_words("hello world")
        assert isinstance(result, int)

    def test_celsius_to_fahrenheit_returns_numeric(self):
        """Ensure celsius_to_fahrenheit returns a numeric type."""
        result = celsius_to_fahrenheit(0)
        assert isinstance(result, (int, float))

    def test_reverse_very_long_string(self):
        """Test reversing a very long string for performance."""
        long_string = "a" * 10000
        result = reverse_string(long_string)
        assert len(result) == 10000
        assert result[0] == "a"
        assert result[-1] == "a"

    def test_count_words_very_long_sentence(self):
        """Test counting words in a very long sentence."""
        long_sentence = " ".join(["word"] * 1000)
        assert count_words(long_sentence) == 1000

    def test_temperature_conversion_consistency(self):
        """Test that C->F conversion is mathematically consistent."""
        # Test that the formula (C * 9/5) + 32 is applied correctly
        celsius = 37.5
        expected = (celsius * 9/5) + 32
        assert celsius_to_fahrenheit(celsius) == expected
