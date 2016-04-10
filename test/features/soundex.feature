Feature: Soundex algorithm

  Scenario Outline: A word is given to soundex algorithm
    Given A soundex instance
    When I enter a word as "<word>"
    Then it is encoded to "<encoded>"

    # the word is the given word
    # encoded is the expected encoded value
    Examples:
      | word               | encoded |
      | A                  | A000    |
      | I                  | I000    |
      | Ab                 | A100    |
      | Ac                 | A200    |
      | Ad                 | A300    |
      | Ax                 | A200    |
      | A#                 | A000    |
      | Acdl               | A234    |
      | Baeiouhycdl        | B234    |
      | Abfcgdt            | A123    |
      | BaAeEiIoOuUhHyYcdl | B234    |
      | Bbcd               | B230    |
      | Jbob               | J110    |

  Scenario: A word is given to soundex algorithm
    Given A soundex instance
    When I enter the word "Dcdlb"
    Then the encoded length is equal to "4u"

  Scenario: A word is given to soundex algorithm with lower case letter
    Given A soundex instance
    When I enter the lower case word "abcd"
    Then the encoded first letter is equal to "A"

  Scenario Outline: A word is given to soundex algorithm
    Given A soundex instance
    When I enter the character "<character>"
    Then it is equal to other encoded character "<other_character>"
    Examples:
      | character | other_character |
      | b         | f               |
      | c         | g               |
      | d         | t               |

  Scenario Outline: A word is given to soundex algorithm
    Given A soundex instance
    When I enter the string "<string>"
    Then it is equal to other encoded string "<other_string>"
    Examples:
      | string | other_string |
      | BCDL   | Bcdl         |
