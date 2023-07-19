<h1>Fence-Flea-Market-Keeper</h1>

This is a Discord bot designed to provide information about Escape from Tarkov (EFT) items and their current market prices. The bot utilizes the Tarkov API to fetch data about items and calculates their market tier based on their prices. It also offers a brief tutorial on how to use its commands.

<h2>Features</h2>
<ul>
<li>/price [item_name]: Retrieve the current market price and tier of the specified EFT item.</li>
<li>/tier: Display the loot tiers based on slot price identification.</li>
<li>/how2use: Learn how to use the bot and its available commands.</li>
</ul>
<h2>Requirements</h2>
<ul>
<li>Python 3.x</li>
<li>discord.py library (you can install it via pip install discord.py)</li>
<li>requests library (you can install it via pip install requests)</li>
<li>python-dotenv library (you can install it via pip install python-dotenv)</li>
</ul>
<h2>Setup</h2>
<ol>
<li>Clone this repository to your local machine.</li>
<li>Create a Discord bot account through the Discord Developer Portal.</li>
<li>Generate a bot token and copy it.</li>
<li>Rename the .env.example file to .env.</li>
<li>Replace the placeholder YOUR_BOT_TOKEN in the .env file with your actual bot token.</li>
<li>Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.</li>
<li>Open a terminal or command prompt, navigate to the project directory, and run the bot.py file.</li>
</ol>
<h2>Usage</h2>
<ol>
<li>Ensure the bot is running and connected to your Discord server.</li>
<li>Type /how2use in any text channel to get a tutorial on using the bot and available commands.</li>
<li>Use the /price [item_name] command to retrieve the current market price and tier of an EFT item.</li>
<li>Use the /tier command to see the loot tiers based on slot price identification.</li>
</ol>
<h2> Credits </h2>
<ul>
<li>Discord.py Library: https://github.com/Rapptz/discord.py</li>
<li>Escape from Tarkov API: https://tarkov.dev/api/</li>
</ul>
<h2>Contribution</h2>
If you find any issues or have suggestions to improve the bot, feel free to open an issue or submit a pull request.
