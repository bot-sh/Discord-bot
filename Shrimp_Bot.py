import discord

TOKEN = 'Nice Try'  

OWNER_ID = 814869741021560913  

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Set up the client
client = discord.Client(intents=intents)

# Predefined responses
responses = {
    "hi": "Hi there!\n Here are some popular questions you can ask me :\n 1. Who is sulaiman\n 2. Who is nerhea\n 3. Who is Nakshatra \n 4. Who has the same weight as a Hippo \n 5. Who is most unlikely to get a job\n 6. Who is Dushanth \nStay tuned for other responses!",
    "who is sulaiman": "<@814869741021560913> is one of the funniest people alive rn",
    "who is nerhea": "<@869981593547202621> is a 5'1 who got 79% 10th CBSE who wakes up at 6am to study maths 🤓",
    "who is nakshatra": "<@1283308964465082370> She is 4'1 (barely taller than that annoying cat she has) who only plays roblox 24/7",
    "who has the same weight as a hippo": "On everyone's soul it is Ruquia (<@1064629697192931348>)",
    "who is dushanth": "<@804705890165850113> is the one and only husband of <@869981593547202621>",
    "who is most unlikely to get a job": "Everybody and their Mom's know that it is <@1134879775865970778>",
}

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # ✅ Owner-only DM command to send a message to a matched channel
    if isinstance(message.channel, discord.DMChannel):
        if message.author.id == OWNER_ID and message.content.startswith("!say "):
            parts = message.content.split(" ", 2)
            if len(parts) < 3:
                await message.channel.send("⚠️ Usage: `!say <channel-name> <your message>`")
                return

            target_suffix = parts[1].lower()
            msg = parts[2]

            for guild in client.guilds:
                for channel in guild.text_channels:
                    if channel.name.lower().endswith(target_suffix):
                        await channel.send(msg)
                        await message.channel.send(f"✅ Sent to #{channel.name}")
                        return

            await message.channel.send("❌ Channel not found.")
            return

    # ✅ Respond to being mentioned or "@bot help" like "hi"
    if client.user in message.mentions:
        content = message.content.lower()
        
        # If message is only a mention or contains 'help', treat it as 'hi'
        if content.strip() == f"<@{client.user.id}>" or "help" in content:
            await message.channel.send(responses["hi"])
            return

        for question, reply in responses.items():
            if question in content:
                await message.channel.send(reply)
                return

        await message.channel.send("Wrong command, get better!")

# Run the bot
client.run(TOKEN)
