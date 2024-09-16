import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Classe que representa a calculadora
class CalculatorView(View):
    def __init__(self, user):
        super().__init__(timeout=60)
        self.expression = ""
        self.user = user

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.user:
            await interaction.response.send_message("Você não pode usar esta calculadora.", ephemeral=True)
            return False
        return True

    # Botão para os números e operadores
    @discord.ui.button(label="1", style=discord.ButtonStyle.secondary)
    async def one(self, interaction: discord.Interaction, button: Button):
        self.expression += "1"
        await self.update_display(interaction)

    @discord.ui.button(label="2", style=discord.ButtonStyle.secondary)
    async def two(self, interaction: discord.Interaction, button: Button):
        self.expression += "2"
        await self.update_display(interaction)

    @discord.ui.button(label="3", style=discord.ButtonStyle.secondary)
    async def three(self, interaction: discord.Interaction, button: Button):
        self.expression += "3"
        await self.update_display(interaction)

    @discord.ui.button(label="C", style=discord.ButtonStyle.danger)
    async def clear(self, interaction: discord.Interaction, button: Button):
        self.expression = ""
        await self.update_display(interaction)

    @discord.ui.button(label="+", style=discord.ButtonStyle.primary)
    async def add(self, interaction: discord.Interaction, button: Button):
        self.expression += "+"
        await self.update_display(interaction)

    @discord.ui.button(label="4", style=discord.ButtonStyle.secondary)
    async def four(self, interaction: discord.Interaction, button: Button):
        self.expression += "4"
        await self.update_display(interaction)

    @discord.ui.button(label="5", style=discord.ButtonStyle.secondary)
    async def five(self, interaction: discord.Interaction, button: Button):
        self.expression += "5"
        await self.update_display(interaction)

    @discord.ui.button(label="6", style=discord.ButtonStyle.secondary)
    async def six(self, interaction: discord.Interaction, button: Button):
        self.expression += "6"
        await self.update_display(interaction)

    @discord.ui.button(label="-", style=discord.ButtonStyle.primary)
    async def subtract(self, interaction: discord.Interaction, button: Button):
        self.expression += "-"
        await self.update_display(interaction)

    @discord.ui.button(label="7", style=discord.ButtonStyle.secondary)
    async def seven(self, interaction: discord.Interaction, button: Button):
        self.expression += "7"
        await self.update_display(interaction)

    @discord.ui.button(label="8", style=discord.ButtonStyle.secondary)
    async def eight(self, interaction: discord.Interaction, button: Button):
        self.expression += "8"
        await self.update_display(interaction)

    @discord.ui.button(label="9", style=discord.ButtonStyle.secondary)
    async def nine(self, interaction: discord.Interaction, button: Button):
        self.expression += "9"
        await self.update_display(interaction)

    @discord.ui.button(label="*", style=discord.ButtonStyle.primary)
    async def multiply(self, interaction: discord.Interaction, button: Button):
        self.expression += "*"
        await self.update_display(interaction)

    @discord.ui.button(label="0", style=discord.ButtonStyle.secondary)
    async def zero(self, interaction: discord.Interaction, button: Button):
        self.expression += "0"
        await self.update_display(interaction)

    @discord.ui.button(label="=", style=discord.ButtonStyle.success)
    async def equals(self, interaction: discord.Interaction, button: Button):
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "Erro"
        await self.update_display(interaction)

    @discord.ui.button(label="/", style=discord.ButtonStyle.primary)
    async def divide(self, interaction: discord.Interaction, button: Button):
        self.expression += "/"
        await self.update_display(interaction)

    async def update_display(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Calculadora simples com discord.py", description=f"```\n{self.expression}\n```")
        await interaction.response.edit_message(embed=embed, view=self)

# Comando para chamar a calculadora
@bot.hybrid_command(name="calculadora", description="Abre uma calculadora interativa.")
async def calculadora(ctx: commands.Context):
    view = CalculatorView(user=ctx.author)
    embed = discord.Embed(title="Calculadora simples com discord.py", description="```\n...\n```")
    await ctx.send(embed=embed, view=view)

# Evento para indicar que o bot está online
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Sincronizados {len(synced)} comandos slash.")
    except Exception as e:
        print(e)

# Substitua o 'YOUR_BOT_TOKEN' pelo token real do seu bot
bot.run('TOKEN_DO_SEU_BOT')
