# flashcards-telegram-bot
[@memo_flashcards_bot](https://t.me/memo_flashcards_bot)

### MongoDB Document Sample
Account
```
{
  "userId": 1,
  "reminder": true,
  "categories": {
    "English": [
      {
        "deckName": "Body Parts",
        "lastUsed": 1657033667,
        "favorite": true,
        "cards": [
          {
            "fileId": 11,
            "frontSide": "arm",
            "backSide": "рука"
          }
        ]
      }
    ]
  }
}
```

Distribution
```
{
  "active": true,
  "frequency": "hour / day / week / month",
  "last_repeat": <timestamp>,
  "first_repeat": <timestamp>,
  "remaining_repeats": 12, 
}
```
