Feature Trademe listing
  Scenario:  Search Listing in Trademe
    Given Open trademe sanbox website
    When verify trademe homepage
    Then search for "item"
    And Close browser
