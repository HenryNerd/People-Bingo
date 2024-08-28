import discord

TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

   
    channel = client.get_channel(1278138407524237376)

    @bot.tree.command(name="ping", description="Says hello!")
    async def ping(interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong')
client.run(TOKEN)