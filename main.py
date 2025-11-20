import os
import json
import random
import discord
from discord import app_commands
from flask import Flask
from threading import Thread

# ==========================
# CONFIGURAÇÃO DE CANAIS
# ==========================
CONFIG_FILE = "command_channels.json"

if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        command_channels = json.load(f)
else:
    command_channels = {}

def save_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(command_channels, f, indent=4)


# ==========================
#   CLIENTE / BOT
# ==========================
class Rq(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} está ligado!")


bot = Rq()

# ==========================
#   COMANDO AJUDA
# ==========================
@bot.tree.command(name="ajuda", description="Veja a lista de comandos disponíveis")
async def ajuda(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Olá! Aqui está a lista de comandos:\n"
        "`/nmasc` — Nome masculino\n"
        "`/nfem` — Nome feminino\n"
        "`/nmm` — Nome medieval masculino\n"
        "`/nmf` — Nome medieval feminino\n"
        "`/rolar` — Rolar dados (ex: 2d20, 3d6)\n",
        ephemeral=True
    )
# ==========================
#   CONVITE QUE DÁ CARGO
# ==========================

# Armazena: { "invite_code": role_id }
invite_roles = {}

@bot.tree.command(name="convitecargo", description="Cria um convite que dá um cargo automaticamente")
@app_commands.describe(cargo="Selecione o cargo que será aplicado ao entrar")
async def convitecargo(interaction: discord.Interaction, cargo: discord.Role):

    # Criar convite no canal atual
    invite = await interaction.channel.create_invite(max_uses=1, unique=True)

    # Salvar código → cargo
    invite_roles[invite.code] = cargo.id

    await interaction.response.send_message(
        f"🎫 Convite criado!\n"
        f"Use este link: **https://discord.gg/{invite.code}**\n"
        f"📌 Quem entrar por ele receberá automaticamente o cargo **{cargo.name}**.",
        ephemeral=True
    )


# Detectar quando alguém entra pelo convite
@bot.event
async def on_member_join(member: discord.Member):
    # Pegar convites antes e depois
    guild = member.guild
    invites_after = await guild.invites()

    for invite in invites_after:
        # Verifica se o convite é um dos convites especiais
        if invite.code in invite_roles:
            role_id = invite_roles[invite.code]
            role = guild.get_role(role_id)

            if role:
                await member.add_roles(role, reason="Entrou pelo convite especial")
                print(f"{member} recebeu o cargo {role.name} pelo convite {invite.code}")

            # Remover depois de usado (evita erros)
            invite_roles.pop(invite.code, None)
            break




# ==========================
#   NOMES ALEATÓRIOS
# ==========================

@bot.tree.command(name="nmasc", description="Gera um nome masculino aleatório")
async def masc(interaction: discord.Interaction):
    nomes = [
     "Arthur", "Miguel", "Heitor", "Theo", "Gael",
    "Benício", "Samuel", "Davi", "Gabriel", "Lorenzo",
    "Pedro", "Isaac", "Noah", "Daniel", "Lucas",
    "Gustavo", "Antônio", "Enzo", "Benjamin", "Otávio",
    "Leonardo", "Cauã", "Bryan", "Felipe", "Raul",
    "Willy", "Hugo", "Murilo", "Elias", "Calebe",
    "Yago", "Caio", "Vicente", "João", "Emanuel",
    "Nicolas", "Kevin", "Marcos", "Rodrigo", "Bruno",
    "André", "Thiago", "Diego", "Vitor", "Matheus",
    "Eduardo", "Levi", "Pietro", "Igor", "Vinícius",
    "Lucca", "Henry", "Otto", "Jonathan", "Paulo",
    "Júlio", "Renan", "Fernando", "William", "Willy",
    "Victor Hugo", "Eric", "Adrian", "Ruan", "Allan",
    "Cristian", "Nelson", "Estevão", "Fabrício", "Giovanni",
    "Kai", "Ruan", "Edgar", "Marlon", "Tales",
    "Eron", "César", "Alexandre", "Rodolfo", "Victor Hugo",
    "Iago", "Edson", "Anderson", "Douglas", "Rogério",
    "Dener", "Anthony", "Eric", "Marcelo", "Osvaldo",
    "Renato", "Luciano", "Everaldo", "Filipe", "Wagner",
    "Kevin", "Luan", "Augusto", "Sérgio", "Felix"
    ]
    await interaction.response.send_message(
        f"🧙 Nome masculino gerado: **{random.choice(nomes)}**",
        ephemeral=True
    )


@bot.tree.command(name="nfem", description="Gera um nome feminino aleatório")
async def fem(interaction: discord.Interaction):
    nomes = [
      "Alice", "Helena", "Milena", "Laura", "Sophia",
    "Isabella", "Heloísa", "Cecília", "Beatriz", "Eloá",
    "Maria Luiza", "Esther", "Antonella", "Sarah", "Isadora",
    "Melissa", "Lara", "Giovanna", "Yasmin", "Luiza",
    "Mariana", "Nicole", "Aurora", "Clara", "Vitória",
    "Maya", "Lívia", "Bianca", "Camila", "Júlia",
    "Rafaela", "Alícia", "Lorena", "Gabriela", "Pietra",
    "Lavínia", "Bruna", "Stella", "Carolina", "Ana Júlia",
    "Rebeca", "Luna", "Ana Laura", "Agatha", "Sophie",
    "Mirella", "Elisa", "Eduarda", "Marina", "Olívia",
    "Clarice", "Daniela", "Vanessa", "Patrícia", "Talita",
    "Simone", "Débora", "Sabrina", "Larissa", "Daniele",
    "Paloma", "Mimi", "Manuela", "Kaline", "Fernanda",
    "Tatiane", "Priscila", "Carla", "Cláudia", "Fabiana",
    "Letícia", "Evelyn", "Gabrielly", "Lorraine", "Nina",
    "Tainá", "Selena", "Morgana", "Vera", "Juliana",
    "Jade", "Natália", "Cíntia", "Adriana", "Aline",
    "Samara", "Eliane", "Joana", "Bárbara", "Heloise",
    "Ivete", "Rayssa", "Milena", "Maitê", "Rúbia",
    "Cristina", "Iara", "Yasmin", "Noemi", "Malu"
    ]
    await interaction.response.send_message(
        f"🧙 Nome feminino gerado: **{random.choice(nomes)}**",
        ephemeral=True
    )


@bot.tree.command(name="nmm", description="Gera nome masculino medieval")
async def medieval_m(interaction: discord.Interaction):
    nomes = [
        "Alaric", "Cedric", "Edric", "Godfrey", "Roland", "Leofric", "Oswin", "Baldric", "Ulric", "Aldred",
"Arthas", "Gareth", "Luther", "Darian", "Theron", "Roderick", "Tristan", "Hadrian", "Lucan", "Eldric",
"Sigurd", "Aldric", "Wulfric", "Theobald", "Geralt", "Soren", "Dorian", "Faolan", "Kael", "Tavian",
"Erendir", "Vorstag", "Merek", "Drystan", "Rowan", "Kaelen", "Evander", "Aeran", "Caelan", "Rhydan",
"Arden", "Cyran", "Darian", "Fenric", "Iskandar", "Magnus", "Orin", "Sirius", "Valen", "Zephyr", "Arden", "Rowan", "Ash", "Lyric", "Sage", "Avery", "Riven", "Eris", "Nova", "Lior",
"Kael", "Raine", "Ember", "Vale", "Orion", "Sky", "Lux", "Aeris", "Cyan", "Ren",
"Tarian", "Sol", "Mika", "Kairen", "Onyx", "Aster", "Eden", "Briar", "Nix", "Haven"
    ]
    await interaction.response.send_message(
        f"🧙 Nome medieval masculino gerado: **{random.choice(nomes)}**",
        ephemeral=True
    )


@bot.tree.command(name="nmf", description="Gera nome feminino medieval")
async def medieval_f(interaction: discord.Interaction):
    nomes = [
        "Elowen", "Seraphine", "Lyanna", "Aria", "Evelyn", "Selene", "Isolde", "Rowena", "Aeloria", "Ygritte",
"Freyja", "Lilith", "Astrid", "Celestia", "Marienne", "Ravena", "Arielle", "Talia", "Elysia", "Odette",
"Nymeria", "Avaline", "Elara", "Kyria", "Maelis", "Soraya", "Thalassa", "Vespera", "Zephira", "Lunara",
"Aeris", "Nerissa", "Valkyra", "Seren", "Velaria", "Ylanna", "Aurelia", "Daphne", "Kallista", "Rhiannon"
"Arden", "Rowan", "Ash", "Lyric", "Sage", "Avery", "Riven", "Eris", "Nova", "Lior",
"Kael", "Raine", "Ember", "Vale", "Orion", "Sky", "Lux", "Aeris", "Cyan", "Ren",
"Tarian", "Sol", "Mika", "Kairen", "Onyx", "Aster", "Eden", "Briar", "Nix", "Haven"
    ]
    await interaction.response.send_message(
        f"🧙 Nome medieval feminino gerado: **{random.choice(nomes)}**",
        ephemeral=True
    )


# ==========================
#   ROLAR DADOS
# ==========================
@bot.tree.command(name="rolar", description="Rola dados no formato XdY (ex: 2d20)")
@app_commands.describe(dado="Formato como 2d20, 3d6, 1d100")
async def rolar(interaction: discord.Interaction, dado: str):
    import re

    match = re.match(r"^(\d+)[dD](\d+)$", dado.strip())
    if not match:
        await interaction.response.send_message(
            "⚠️ Formato inválido. Use algo como `2d20`.",
            ephemeral=True
        )
        return

    qtd = int(match.group(1))
    faces = int(match.group(2))

    if qtd <= 0 or faces <= 0:
        await interaction.response.send_message("⚠️ Use números positivos.", ephemeral=True)
        return
    if qtd > 100:
        await interaction.response.send_message("⚠️ Máximo de **100** dados.", ephemeral=True)
        return

    resultados = [random.randint(1, faces) for _ in range(qtd)]
    total = sum(resultados)

    await interaction.response.send_message(
        f"🎲 **Rolagem:** {qtd}d{faces}\n"
        f"👀 **Resultados:** {', '.join(map(str, resultados))}\n"
        f"⚔️ **Total:** {total}"
    )


# ==========================
#   FLASK (KEEP ALIVE)
# ==========================
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot online!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_flask, daemon=True).start()


# ==========================
#   INICIAR BOT
# ==========================
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
