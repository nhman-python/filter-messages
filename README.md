# Filter Word

Filter Word Bot is a Telegram bot designed to filter messages in group chats based on predefined keywords.

## Features

— Filters messages containing specific words or phrases.
— Actions can be taken on filtered messages, such as banning, restricting, or deleting.

## Installation

1. Clone the repository:

   ```bash
   https://github.com/nhman-python/filter-messages.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure bot settings:

   - Open `index.py` and update the following variables:
     - `API_ID`: Your Telegram API ID.
     - `API_HASH`: Your Telegram API hash.
     - `PHONE_NUMBER`: Your phone number in international format.
     - `SESSION_NAME`: Session name for the bot.
     - `GROUP_ID_FILTER`: ID of the group where filtering will be applied.

4. edit `filter-list.json`:

   - edit a JSON file named `filter-list.json` containing the list of filters and actions. The structure should be as follows:

     ```json
     {
         "ban": ["word1", "word2"],
         "restrict": ["phrase1", "phrase2"],
         "delete": ["test", "hello"]
     }
     ```


## Usage

Run the bot script:

```bash
python index.py
```

Once the bot is running, it will start filtering messages in the specified group chat according to the configured filter list.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or feature additions.

## License

This project is licensed under the [Apache License](https://github.com/nhman-python/filter-messages/blob/main/LICENSE).
