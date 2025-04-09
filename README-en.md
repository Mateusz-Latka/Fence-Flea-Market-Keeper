# Fence-Flea-Market-Keeper

Fence-Flea-Market-Keeper is a Discord bot designed to provide information about Escape from Tarkov (EFT) items and their current market prices. The bot utilizes the Tarkov API to fetch data about items and calculates their prices.

## Features
- `/price [item_name]`: Retrieve the current market price and tier of the specified EFT item.
- `/tier`: Display the loot tiers based on slot price identification.
- `/how2use`: Learn how to use the bot and its available commands.

## Requirements
- Python 3.x
- `discord.py` library
- `requests` library
- `python-dotenv` library

You can install the required libraries with:
```bash
pip install -r requirements.txt
```

## Setup
1. Clone this repository to your local machine.
2. Create a Discord bot account through the [Discord Developer Portal](https://discord.com/developers/applications).
3. Generate a bot token and copy it.
4. Rename the `.env.example` file to `.env`.
5. Replace the placeholder `YOUR_BOT_TOKEN` in the `.env` file with your actual bot token.
6. Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.
7. Open a terminal or command prompt, navigate to the project directory, and run the `bot.py` file.

## Usage
1. Ensure the bot is running and connected to your Discord server.
2. Type `/how2use` in any text channel to get a tutorial on using the bot and available commands.
3. Use the `/price [item_name]` command to retrieve the current market price and tier of an EFT item.
4. Use the `/tier` command to see the loot tiers based on slot price identification.

## Examples
- `/price AK-47`: Retrieves the current market price and tier of the AK-47 item.
- `/tier`: Displays the loot tiers.

## Credits
- [Discord.py Library](https://github.com/Rapptz/discord.py)
- [Escape from Tarkov API](https://tarkov.dev/api/)

## Contribution
If you find any issues or have suggestions to improve the bot, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or feedback, please open an issue or contact the repository owner.
