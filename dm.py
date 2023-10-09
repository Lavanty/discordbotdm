import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    with open('tokens.txt', 'r') as file:
        tokens = file.readlines()

        for token in tokens:
            token = token.strip()
            try:
                user = await client.fetch_user(int(token))
                await user.send("Hello! This is a message from your Discord bot.")
                print(f"Sent message to {user.name}")
            except Exception as e:
                print(f"Failed to send message to {token}: {e}")

with open('bot_token.txt', 'r') as file:
    bot_token = file.read().strip()

client.run(bot_token)
