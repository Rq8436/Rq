import discord
from discord import app_commands
import random #aqui
import json
import os

CONFIG_FILE = "command_channels.json"

# Carregar canais permitidos
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        command_channels = json.load(f)
else:
    command_channels = {}

def save_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(command_channels, f, indent=4) #até aqui


class Rq(discord.Client):
    def __init__ (self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="n",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print:(f"O Bot {self.user} está ligado! ")

bot=Rq()

@bot.tree.command(name="ajuda",description="use esse comando para descobrir novos comandos do Bot do RPGzerando")
async def ajuda(Interaction:discord.Interaction):
    await Interaction.response.send_message("Olá, esse é o Bot do RPGZerando!\n\nTemos os comandos:\n`nmasc` — gera um nome masculino aleatório\n`nfem` — gera um nome feminino aleatório\n`nmm` — gera um nome medieval masculino aleatório\n`nmf` — gera um nome medieval feminino aleatório"
, ephemeral=True
)

@bot.tree.command(name="nmasc", description="Gera um nome masculino aleatório")
async def slash_nmasc(interaction: discord.Interaction):
    nomes_masculinos = [
       "Arthur", "Miguel", "Heitor", "Theo", "Davi", "Gabriel", "Bernardo", "Samuel", "Pedro", "Gael",
    "Ravi", "Isaac", "Benjamin", "Guilherme", "Nicolas", "João", "Lorenzo", "Daniel", "Gal", "Lucas",
    "Enzo", "Leonardo", "Bryan", "Caio", "Henry", "Lucca", "Gustavo", "Vinícius", "Eduardo", "Antônio",
    "Noah", "João Miguel", "Vicente", "Renato", "Otávio", "Emanuel", "Murilo", "Yago", "Kevin", "Felipe",
    "Anthony", "Thomas", "André", "Cauã", "Levi", "Francisco", "Isaías", "Calebe", "Augusto", "Alexandre",
    "Diego", "Igor", "Nathan", "Bryan", "Raul", "Fabrício", "Danilo", "Vitor", "Dylan", "Marcos",
    "Rodrigo", "Paulo", "Pietro", "Ruan", "Dener", "Douglas", "Cristian", "Elias", "Hugo", "Estevão",
    "Tiago", "Jonathan", "Anderson", "Rafael", "Jonas", "Natan", "Adriel", "Edu", "Luan", "Marcelo",
    "Eron", "Filipe", "Victor", "César", "Gabriell", "Marlon", "Renan", "Otto", "Diogo", "Caetano",
    "Allan", "Edgar", "Adriano", "William", "André Luiz", "Eric", "Dener", "Rogério", "Fernando", "Júlio"
    ]
    nome = random.choice(nomes_masculinos)
    await interaction.response.send_message(f"🧙 Nome masculino gerado: **{nome}**",ephemeral=True)

@bot.tree.command(name="nfem", description="Gera um nome feminino aleatório")
async def slash_nmasc(interaction: discord.Interaction):
    nomes_femininos = [
       "Alice", "Sophia", "Helena", "Valentina", "Laura", "Isabella", "Heloísa", "mimi", "Júlia", "Luiza",
    "Lorena", "Lívia", "Giovanna", "Maria Clara", "Cecília", "Eloá", "Beatriz", "Maria Luiza", "Esther", "Antonella",
    "Sarah", "Isadora", "Melissa", "Yasmin", "Isabelly", "Lavínia", "Alícia", "Lara", "Emanuelly", "Ana Júlia",
    "Rebeca", "Agatha", "Stella", "Marina", "Gabriela", "Olívia", "Letícia", "Bianca", "Vitória", "Carolina",
    "Clara", "Rafaela", "Marcela", "Elisa", "Ana Laura", "Eduarda", "Camila", "Maitê", "Clarice", "Aurora",
    "Fernanda", "Pietra", "Maya", "Sophie", "Maria Eduarda", "Catarina", "Maria Alice", "Luna", "Ana Lívia", "Mariana",
    "Amanda", "Nicole", "Bruna", "Giulia", "Juliana", "Isis", "Rayssa", "Talita", "Natália", "Jade",
    "Paola", "Milena", "Ana Beatriz", "Laís", "Alana", "Heloise", "Tatiane", "Vitória", "Cláudia", "Mirella",
    "Débora", "Sabrina", "Daniela", "Cíntia", "Patrícia", "Carla", "Vanessa", "Fabiana", "Leticia", "Evelyn",
    "Brenda", "Lorraine", "Rúbia", "Tatiana", "Melissa", "Renata", "Gabrielly", "Manoela", "Eduarda", "Luana""Alice", "Helena", "Valentina", "Laura", "Manuela", "Isabella", "Heloísa", "Maria Clara", "Cecília", "Eloá",
    "Beatriz", "Maria Luiza", "Antonella", "Sarah", "Isadora", "Melissa", "Yasmin", "Isabelly", "Lavínia", "Lara",
    "Emanuelly", "Rebeca", "Agatha", "Stella", "Marina", "Gabriela", "Olívia", "Letícia", "Bianca", "Vitória",
    "Carolina", "Clara", "Rafaela", "Marcela", "Elisa", "Eduarda", "Camila", "Maitê", "Clarice", "Aurora",
    "Fernanda", "Pietra", "Maya", "Sophie", "Catarina", "Maria Alice", "Luna", "Mariana", "Amanda", "Nicole",
    "Bruna", "Giulia", "Juliana", "Isis", "Rayssa", "Ivete", "Natália", "Jade", "Paola", "Milena",
    "Alana", "Heloise", "Tatiane", "Laís", "Cláudia", "Mirella", "Débora", "Sabrina", "Daniela", "Cíntia",
    "Patrícia", "Carla", "Vanessa", "Fabiana", "Letícia", "Evelyn", "Brenda", "Lorraine", "Tatiana", "Renata",
    "Manoela", "Luana", "Adriana", "Aline", "Samara", "Eliane", "Priscila", "Joana", "Bárbara", "Morgana",
    "Vera", "Nina", "Tainá", "Celina", "Rúbia", "Cristina", "Iara", "Selena", "Rafaela", "Simone"
    ]
    nomef = random.choice(nomes_femininos)
    await interaction.response.send_message(f"🧙 Nome feminino gerado: **{nomef}**", ephemeral=True)


@bot.tree.command(name="nmm", description="Gera um nome masculino medieval aleatório")
async def slash_nmasc(interaction: discord.Interaction):
    nomes_medievaismasculinos = [
        "Alaric", "Cedric", "Edric", "Godfrey", "Roland", "Leofric", "Oswin", "Baldric", "Ulric", "Aldred",
    "Arthas", "Gareth", "Luther", "Darian", "Theron", "Roderick", "Tristan", "Hadrian", "Lucan", "Eldric",
    "Magnus", "Gideon", "Tobias", "Dorian", "Rowan", "Everard", "Drystan", "Silas", "Lancel", "Cassian",
    "Corvin", "Brandr", "Sigmund", "Hector", "Beren", "Torvald", "Ronan", "Edwin", "Gerard", "Aurelian",
    "Caius", "Marek", "Leoric", "Severin", "Jareth", "Fenric", "Arvid", "Ragnar", "Thorin", "Eamon",
    "Lucien", "Valen", "Darion", "Tarian", "Aldwin", "Merrick", "Osric", "Garreth", "Rufus", "Draven",
    "Taren", "Eldwin", "Corvinus", "Varric", "Kael", "Hadric", "Sylas", "Alban", "Brynjar", "Durand",
    "Beric", "Erwin", "Galen", "Torin", "Oberon", "Sigfreuld", "Arden", "Cedan", "Thane", "Merek",
    "Fendrel", "Corwyn", "Lucius", "Balric", "Theran", "Roderic", "Emric", "Levan", "Jareth", "Oren",
    "Bastian", "Adric", "Garrick", "Ulfric", "Darian", "Edras", "Kelric", "Osbert", "Rainard", "Thallan", "Aldric", "Balin", "Cedwyn", "Draven", "Edwyn", "Fendrel", "Garron", "Halric", "Ivar", "Jorund",
    "Kaelan", "Lothar", "Maeron", "Neryn", "Osmund", "Perrin", "Quintus", "Rhodric", "Sigurd", "Tavion",
    "Ulmar", "Varyn", "Wulfric", "Yorik", "Zephar", "Alstan", "Berengar", "Caiwen", "Dareth", "Edran",
    "Faelan", "Godric", "Hadric", "Ingram", "Jaric", "Kendric", "Leoric", "Maelor", "Nareth", "Orin",
    "Padrig", "Quintar", "Rennar", "Sorin", "Torric", "Ulricson", "Vaelen", "Wendric", "Ysmar", "Zarek",
    "Aelar", "Brynden", "Corvan", "Dain", "Eirik", "Fenrin", "Gareth", "Hadrin", "Isen", "Jarethor",
    "Korran", "Lorien", "Merek", "Norric", "Orren", "Perric", "Quillon", "Rurik", "Serin", "Thane",
    "Ulfred", "Varek", "Warrin", "Yoren", "Almar", "Branth", "Cador", "Darian", "Eldran", "Faren",
    "Galdor", "Helrik", "Ison", "Jothric", "Kaelric", "Luthar", "Merrin", "Noland", "Orick", "Perron",
    "Quintarion", "Rastan", "Soren", "Torren", "Ulthor", "Valric", "Wendell", "Yurik", "Zennar", "Eldar"]
    nomemm = random.choice(nomes_medievaismasculinos)
    await interaction.response.send_message(f"🧙 Nome medieval gerado: **{nomemm}**", ephemeral=True)


@bot.tree.command(name="nmf", description="Gera um nome feminino medieval aleatório")
async def slash_nmasc(interaction: discord.Interaction):
    nomes_medievaisfemininos = [
        "Aelina", "Brienne", "Cerys", "Delara", "Elowen", "Fiora", "Gwyneth", "Helmine", "Isolde", "Jessara",
    "Kaelin", "Lyra", "Mireth", "Neryssa", "Olwen", "Perwen", "Quilla", "Rowena", "Seraphine", "Tamsin",
    "Urith", "Valeria", "Wendara", "Ysoria", "Zarina", "Adelyn", "Belira", "Catrin", "Daenira", "Eirlys",
    "Fendria", "Gisela", "Hannelore", "Ilara", "Junelle", "Kareen", "Luneth", "Marella", "Nerwen", "Ophelia",
    "Prisca", "Rhiannon", "Selene", "Thalira", "Umbria", "Velora", "Wynneth", "Ylva", "Zahra", "Amariel",
    "Brynna", "Clariel", "Dorethea", "Evelisse", "Faelwen", "Gwenora", "Halene", "Isara", "Jordaine", "Katrisse",
    "Leira", "Mirabel", "Nolwen", "Orinthia", "Philena", "Roswyn", "Saphira", "Tiriel", "Uldra", "Venyra",
    "Wrenna", "Ysolde", "Zynara", "Aveline", "Briselle", "Cedara", "Dahlia", "Elaria", "Feriel", "Griselda",
    "Hestia", "Ilyra", "Jasenne", "Kairen", "Lunara", "Maerwen", "Nadira", "Ophira", "Phaedra", "Ravena",
    "Sylwen", "Thandria", "Ulwynn", "Valleria", "Wynne", "Ysandra", "Zerina", "Arwen", "Briella", "Celestria",
    "Daria", "Eldira", "Fiona", "Galwen", "Helene", "Ismena", "Jordis", "Kallista", "Lirael", "Morrighan",
    "Neryn", "Ondine", "Petra", "Quinara", "Rhoswen", "Selina", "Taryn", "Una", "Violetta", "Wendolin",
    "Yvaine", "Zephyra", "Alarice", "Bellara", "Corinne", "Delwyn", "Eowyn", "Fayeth", "Genevra", "Hester",
    "Irelia", "Jovienne", "Keira", "Lunethra", "Melisandre", "Nadeline", "Orlaith", "Penryn", "Rhiella", "Serilda",
    "Tanith", "Ulrica", "Vanya", "Wynaria", "Ysmira", "Zelara", "Aislin", "Brynja", "Cassara", "Dorella", "Elandra",
    "Fynara", "Gwenlyn", "Hadria", "Idara", "Jasira", "Karelia", "Leona", "Miraine", "Neressa", "Oriana",
    "Phelira", "Rosalinde", "Sariel", "Tiriane", "Urielle", "Verena", "Wenria", "Ysoriah", "Zariel", "Anwyn",
    "Blythe", "Celisse", "Doreth", "Evaria", "Fioraen", "Glenys", "Helara", "Ilwen", "Jorielle", "Kendara",
    "Liliane", "Maelis", "Neryth", "Odira", "Priscelle", "Ravira", "Selandra", "Tanelle", "Urdwyn", "Virelle",
    "Wenyth", "Ydris", "Zirelia", "Aradia", "Belwen", "Cyndra", "Darelle", "Elspeth", "Frida", "Grainne",
    "Hilde", "Isola", "Jolira", "Katriel", "Lunarae", "Miriel", "Noralyn", "Ophelene", "Pyrrha", "Rowenna"
        ]
    nomemf = random.choice(nomes_medievaisfemininos)
    await interaction.response.send_message(f"🧙 Nome feminino medieval gerado: **{nomemf}**", ephemeral=True)



@bot.tree.command(name="rolar", description="Rola dados no formato XdY (ex: 2d20, 3d6, 1d100)")
@app_commands.describe(
    dado="Formato da rolagem (ex: 2d20, 3d6, 1d100)"
)
async def rolar(interaction: discord.Interaction, dado: str):
    import random, re

    # Verifica se o formato é válido (ex: 2d20)
    match = re.match(r"^(\d+)[dD](\d+)$", dado.strip())
    if not match:
        await interaction.response.send_message("⚠️ Use o formato correto, ex: `2d20` ou `3d6`.", ephemeral=True)
        return

    quantidade = int(match.group(1))
    lados = int(match.group(2))

    # Limites de segurança
    if quantidade <= 0 or lados <= 0:
        await interaction.response.send_message("⚠️ Use apenas números positivos!", ephemeral=True)
        return
    if quantidade > 100:
        await interaction.response.send_message("⚠️ O máximo é 100 dados por vez.", ephemeral=True)
        return

    # Rolar os dados
    resultados = [random.randint(1, lados) for _ in range(quantidade)]
    total = sum(resultados)

    # Montar resposta
    detalhes = ", ".join(str(r) for r in resultados)
    resposta = f"🎲 **Rolagem:** {quantidade}d{lados}\n👀 **Resultados:** {detalhes}\n⚔️ **Total:** {total}"

    await interaction.response.send_message(resposta)
#comando keep-alive
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot online!"

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()


bot.run(os.getenv("DISCORD_TOKEN"))
