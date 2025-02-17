import discord
from discord import app_commands

# Defina o ID do seu servidor
id_do_servidor =   

# Criando a classe do bot
class client(discord.Client):
    def __init__(self):
        # Configurando intents necessárias
        intents = discord.Intents.default()
        intents.messages = True  # Permite acessar mensagens
        intents.message_content = True  # Necessário para analisar o conteúdo das mensagens
        intents.guilds = True  # Permite interagir com os servidores
        intents.members = True  # Permite acessar informações dos membros
        super().__init__(intents=intents)
        self.synced = False  # Para evitar sincronizar comandos múltiplas vezes

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True
        print(f"Bot conectado como {self.user}")

# Criando o bot e o sistema de comandos
aclient = client()
tree = app_commands.CommandTree(aclient)

#  Comando 1: Teste simples para ver se o bot está online
@tree.command(guild=discord.Object(id=id_do_servidor), name="teste", description="Verifica se o bot está online")
async def teste(interaction: discord.Interaction):
    await interaction.response.send_message("Estou funcionando! ✅", ephemeral=True)

#  Comando 2: Apaga todas as mensagens de um usuário ativo no servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name="clearuser", description="Apaga mensagens de um usuário ativo")
async def clearuser(interaction: discord.Interaction, user: discord.Member):
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=1000, check=lambda m: m.author == user)
    await interaction.followup.send(f"Foram apagadas {len(deleted)} mensagens de {user.mention}.", ephemeral=True)

# 🗑 Comando 3: Apaga mensagens de um usuário que já saiu do servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name="clearuserleft", description="Apaga mensagens de um usuário que saiu do servidor")
async def clearuserleft(interaction: discord.Interaction, username: str):
    await interaction.response.defer(ephemeral=True)
    deleted = await interaction.channel.purge(limit=1000, check=lambda m: m.author.name == username)

    if deleted:
        await interaction.followup.send(f"Foram apagadas {len(deleted)} mensagens de `{username}`.", ephemeral=True)
    else:
        await interaction.followup.send(f"Nenhuma mensagem encontrada para `{username}`.", ephemeral=True)

# 🎲 Comando 4: Rola um dado de 6 lados
import random

@tree.command(guild=discord.Object(id=id_do_servidor), name="dado", description="Rola um dado de 6 lados")
async def rolar_dado(interaction: discord.Interaction):
    numero = random.randint(1, 6)
    await interaction.response.send_message(f"🎲 Você rolou um **{numero}**!", ephemeral=True)

#  Comando 5: Envia um meme aleatório
memes = [
    "https://i.imgur.com/W3a6v0N.png",
    "https://i.imgur.com/4l6KzwN.jpeg",
    "https://i.imgur.com/RzicA4j.png"
]

@tree.command(guild=discord.Object(id=id_do_servidor), name="meme", description="Envia um meme aleatório")
async def meme(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(memes))

#  Comando 6: Diz o contrário do que o usuário falar
@tree.command(guild=discord.Object(id=id_do_servidor), name="invert", description="Inverte uma mensagem")
async def invert(interaction: discord.Interaction, texto: str):
    await interaction.response.send_message(texto[::-1])

#  Comando 7: Diz qual música o usuário está ouvindo (se estiver ouvindo algo no Spotify)
@tree.command(guild=discord.Object(id=id_do_servidor), name="spotify", description="Mostra a música que você está ouvindo no Spotify")
async def spotify(interaction: discord.Interaction, user: discord.Member):
    for activity in user.activities:
        if isinstance(activity, discord.Spotify):
            await interaction.response.send_message(f"🎵 {user.mention} está ouvindo **{activity.title}** de **{activity.artist}**.")
            return
    await interaction.response.send_message(f"{user.mention} não está ouvindo nada no Spotify no momento.")

# Iniciando o bot (substitua pelo seu token)
aclient.run("SEU_TOKEN_AQUI")
