from behave import *
from nose.tools import assert_equals

from src.mysoundex import MySoundex

use_step_matcher("re")


@given("A soundex instance")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.soundex = MySoundex()
    print("given_a_soundex_instance ", "\n")


@when('I enter a word as "(?P<word>.+)"')
def step_impl(context, word):
    """
    :type context: behave.runner.Context
    :type word: str
    """
    print("when_i_enter_a_word_as ", word, "\n")
    context.encoded = context.soundex.encode(word)


@then('it is encoded to "(?P<encoded>.+)"')
def step_impl(context, encoded):
    """
    :type context: behave.runner.Context
    :type encoded: str
    """
    print("then_it_is_encoded_to ", encoded,  "\n",  "\n")
    assert_equals(encoded, context.encoded)


@when('I enter the word "([^\"]*)"')
def step_impl(context, word):
    """
    :type context: behave.runner.Context
    """
    print("when_i_enter_the_word_as ", word, "\n")
    context.encoded = context.soundex.encode(word)


@then('the encoded length is equal to "([^\"]*)"')
def step_impl(context, length):
    """
    :type context: behave.runner.Context
    """
    print("then_the_encoded_length_is_equal_to ", length, "\n")
    assert_equals(length, len(context.encoded))


@when('I enter the lower case word "([^\"]*)"')
def step_impl(context, word):
    """
    :type context: behave.runner.Context
    """
    print("when_i_enter_the_lower_case_word ", word, "\n")
    context.encoded = context.soundex.encode(word)


@then('the encoded first letter is equal to "([^\"]*)"')
def step_impl(context, letter):
    """
    :type context: behave.runner.Context
    """
    print("then_the_encoded_first_letter_is_equal_to", letter, "\n")
    assert_equals(letter, context.encoded[0])


@when('I enter the character "(?P<character>.+)"')
def step_impl(context, character):
    """
    :type context: behave.runner.Context
    :type character: str
    """
    print("when_i_enter_the_character ", character, "\n")
    context.encoded = context.soundex.encoded_digit(character)


@then('it is equal to other encoded character "(?P<other_character>.+)"')
def step_impl(context, other_character):
    """
    :type context: behave.runner.Context
    :type other_character: str
    """
    print("then_it_is_equal_to_other_encoded_character ", other_character, "\n")
    other_encoded_char = context.soundex.encoded_digit(other_character)
    assert_equals(context.encoded, other_encoded_char)


@when('I enter the string "(?P<string>.+)"')
def step_impl(context, string):
    """
    :type context: behave.runner.Context
    :type string: str
    """
    print("when_i_enter_the_string ", string, "\n")
    context.encoded = context.soundex.encode(string)


@then('it is equal to other encoded string "(?P<other_string>.+)"')
def step_impl(context, other_string):
    """
    :type context: behave.runner.Context
    :type other_string: str
    """
    print("then_it_is_equal_to_other_encoded_string ", other_string, "\n")
    other_encoded_string = context.soundex.encode(other_string)
    assert_equals(context.encoded, other_encoded_string)
