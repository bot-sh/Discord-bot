import discord

# Define your bot's token
TOKEN = '' # Token

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Set up the client
client = discord.Client(intents=intents)

# Define your predefined responses (not case sensitive)
responses = {
    "hi": "Hi there!\n Here are some popular questions you can ask me :\n 1.Who is sulaiman\n Who is nehRIYA\n Who is Nakshatra \n Who has the same weight as a Hippo \n Who is most unlikely to get a job \n stay tuned for other responses",
    "Who is sulaiman": "<@814869741021560913> is one of the funniest people alive rn",
    "Who is nehRIYA": "<@869981593547202621> is a 5'1 who got 79% 10th CBSE who wakes up at 6am to study maths 🤮 ",
    "Who is Nakshatra": "<@1283308964465082370> She is 4'1 (barely taller than that annoying cat she has) who only plays roblox 24/7", # Nakshatra
    "Who has the same weight as a Hippo": "On everyone's soul it is Ruquia (not in the server so cant tag her)",    
    "Who is most unlikely to get a job": "Everybody and their Mom's no that it is <@1134879775865970778>", #Rahul
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == client.user:
        return

    # Check if the bot was mentioned (pinged)
    if client.user in message.mentions:
        content = message.content.lower()
        
        for question, reply in responses.items():
            if question in content:
                await message.channel.send(reply)
                return

        # Default reply if nothing matched
        await message.channel.send("Sorry, I don't understand that. Try asking something else!")

# Run the bot
client.run(TOKEN)