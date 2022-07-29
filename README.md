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
  "code_name": "",
  "time_params": {
    "active": true,
    "frequency": <interval size in hours>,
    "repeat_time": "HH:MM",
    "manual_repeats": ["DD/MM/YYYY HH:MM", ...],
    "last_repeat": 1657033667,
    "total_repeats": 14,
    "remaining_repeats": 12
  },
  "content": {
    "text": "bla-bla\nblalba...",
    "files": [],
  }
}
```
