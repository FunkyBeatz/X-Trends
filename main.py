import discord
from discord.ext import tasks, commands
import os
import requests
from bs4 import BeautifulSoup
from discord import app_commands
from discord.utils import utcnow
import random

# Set up Discord bot with intents and slash commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Store cooldown timestamps for buttons (custom ID -> timestamp)
button_cooldowns = {}


# Sync slash commands globally
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    print(f'Logged in as {bot.user}')
    # Customize bot presence
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="trending keywords on X"))


# Function to fetch and filter trending keywords by scraping GetDayTrends
def get_trending_keywords(limit=10, popularity=None, category=None):
    try:
        url = "https://getdaytrends.com/united-states/"  # Trends for the US, adjust as needed
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")
        # Find trend items (using the working selector)
        trend_items = soup.select(
            "table.table.table-hover.text-left.clickable.ranking.trends.wider.mb-0 tbody tr td:nth-child(2) a.string"
        )

        # Extract trends, cleaning up text
        all_keywords = [
            item.get_text().strip().replace("#", "") for item in trend_items
            if item.get_text().strip()
        ]
        print(f"Found trends: {all_keywords}")  # Debug: print what we found

        if not all_keywords:  # Fallback if no trends found
            print("No trends found on GetDayTrends, using fallback.")
            return [
                "#TechNews", "#GamingUpdate", "#MusicTrends", "#CryptoBuzz",
                "#FashionNow", "#SportsTalk", "#MoviePremiere", "#TechGadgets",
                "#HealthTips", "#TravelDeals"
            ][:limit]

        # Define categories
        categories = {
            "Tech": ["TechNews", "TechGadgets", "CryptoBuzz"],
            "Entertainment": [
                "MoviePremiere", "GamingUpdate", "MusicTrends", "Fable",
                "Star Wars"
            ],
            "News": ["Epstein", "Medicaid", "Five Eyes", "Guam"],
            "General":
            ["Shakir", "Massie", "Midway", "Gronk", "alessi", "Southwest"]
        }

        # Simulate popularity for each keyword (random for fallback, but could be scraped if available)
        keyword_popularity = {
            keyword: random.choice(["High", "Medium", "Low"])
            for keyword in all_keywords
        }

        # Filter keywords based on popularity and category
        filtered_keywords = []
        for keyword in all_keywords:
            keyword_category = next(
                (cat for cat, terms in categories.items() if keyword in terms),
                "General")
            keyword_pop = keyword_popularity.get(
                keyword, "Medium")  # Default to Medium if not found

            if (popularity is None or keyword_pop == popularity) and (
                    category is None or keyword_category == category):
                filtered_keywords.append(keyword)

        return filtered_keywords[:
                                 limit]  # Return only the requested number of filtered keywords
    except Exception as e:
        print(f"Error fetching trends: {e}")
        return [
            "#TechNews", "#GamingUpdate", "#MusicTrends", "#CryptoBuzz",
            "#FashionNow", "#SportsTalk", "#MoviePremiere", "#TechGadgets",
            "#HealthTips", "#TravelDeals"
        ][:limit]


# Slash command for trending keywords with nested options and filters
@bot.tree.command(name="trending_keywords",
                  description="Get trending keywords from X with filters")
@app_commands.describe(
    hours_ago="How many hours ago to look back (including 'now' for <1 hour)",
    keyword_count="Number of trending keywords to display (1-10, default 10)",
    popularity="Filter trends by popularity (optional)",
    category="Filter trends by category (optional)")
@app_commands.choices(
    hours_ago=[
        app_commands.Choice(name="now", value=0),  # Less than 1 hour ago
        *[app_commands.Choice(name=str(i), value=i)
          for i in range(1, 11)]  # 1–10 hours
    ],
    keyword_count=[
        app_commands.Choice(name=str(i), value=i) for i in range(1, 11)
    ],
    popularity=[
        app_commands.Choice(name="High", value="High"),
        app_commands.Choice(name="Medium", value="Medium"),
        app_commands.Choice(name="Low", value="Low")
    ],
    category=[
        app_commands.Choice(name="Tech", value="Tech"),
        app_commands.Choice(name="Entertainment", value="Entertainment"),
        app_commands.Choice(name="News", value="News"),
        app_commands.Choice(name="General", value="General")
    ])
async def trending_keywords(interaction: discord.Interaction,
                            hours_ago: int,
                            keyword_count: int = 10,
                            popularity: str = None,
                            category: str = None):
    if keyword_count > 10 or keyword_count < 1:
        await interaction.response.send_message(
            "Keyword count must be between 1 and 10.", ephemeral=True)
        return
    if hours_ago > 10 or hours_ago < 0:
        await interaction.response.send_message(
            "Hours ago must be between 0 (now) and 10.", ephemeral=True)
        return

    keywords = get_trending_keywords(keyword_count, popularity, category)

    if keywords:
        # Determine dynamic color based on time of day
        current_hour = utcnow().hour
        if 6 <= current_hour < 12:  # Morning
            color = discord.Color.blue()
        elif 12 <= current_hour < 18:  # Afternoon
            color = discord.Color.green()
        elif 18 <= current_hour < 22:  # Evening
            color = discord.Color.purple()
        else:  # Night
            color = discord.Color.gold()

        # Create first embed for top banner
        embed1 = discord.Embed(color=color  # Match the second embed's color
                               )
        embed1.set_image(url="https://i.imgur.com/Eui1QwM.png")  # Top banner

        # Create second embed for trends, timestamp, banner, and copyright
        embed2 = discord.Embed(
            title="📊 Top Trending Keywords:",
            color=color  # Match the first embed's color
        )
        # Add fields for each keyword (cleaner, without category/popularity text)
        for i, keyword in enumerate(keywords, 1):
            embed2.add_field(
                name=f"#{i}",
                value=keyword,
                inline=True  # This keeps fields side by side
            )
        # Add timestamp as a field, aligned to the right
        embed2.add_field(
            name="\u200b",  # Invisible character for spacing
            value=f"Updated: {utcnow().strftime('%b %d, %Y, %H:%M UTC')}",
            inline=True)
        # Add bottom banner
        embed2.set_image(url="https://i.imgur.com/i9s3LmJ.png")
        # Add copyright text as plain footer
        embed2.set_footer(text="Web Frens 2025 ©")

        view = discord.ui.View(timeout=None)  # Persistent view
        view.add_item(
            discord.ui.Button(label="Refresh Trends",
                              style=discord.ButtonStyle.primary,
                              custom_id="refresh_trends"))

        # Send both embeds together
        await interaction.response.send_message(embeds=[embed1, embed2],
                                                view=view)
    else:
        await interaction.response.send_message(
            "❌ Couldn't fetch trends. Try again later!")


# Button handler for refresh
@bot.event
async def on_interaction(interaction):
    if interaction.type == discord.InteractionType.component and interaction.data[
            "custom_id"] == "refresh_trends":
        # Check cooldown (5 minutes) using button_cooldowns dictionary
        custom_id = interaction.data["custom_id"]
        if custom_id in button_cooldowns and (
                utcnow() - button_cooldowns[custom_id]
        ).total_seconds() < 300:  # 5 minutes
            await interaction.response.send_message(
                "Please wait 5 minutes before refreshing again.",
                ephemeral=True)
            return
        try:
            keywords = get_trending_keywords(
                10, None, None)  # Default to no filters for refresh
            if keywords:
                # Determine dynamic color based on time of day
                current_hour = utcnow().hour
                if 6 <= current_hour < 12:  # Morning
                    color = discord.Color.blue()
                elif 12 <= current_hour < 18:  # Afternoon
                    color = discord.Color.green()
                elif 18 <= current_hour < 22:  # Evening
                    color = discord.Color.purple()
                else:  # Night
                    color = discord.Color.gold()

                # Create first embed for top banner
                embed1 = discord.Embed(
                    color=color  # Match the second embed's color
                )
                embed1.set_image(
                    url="https://i.imgur.com/Eui1QwM.png")  # Top banner

                # Create second embed for trends, timestamp, banner, and copyright
                embed2 = discord.Embed(
                    title="📊 Top Trending Keywords:",
                    color=color  # Match the first embed's color
                )
                # Add fields for each keyword (cleaner, without category/popularity text)
                for i, keyword in enumerate(keywords[:10], 1):
                    embed2.add_field(name=f"#{i}", value=keyword, inline=True)
                # Add timestamp as a field, aligned to the right
                embed2.add_field(
                    name="\u200b",  # Invisible character for spacing
                    value=
                    f"Updated: {utcnow().strftime('%b %d, %Y, %H:%M UTC')}",
                    inline=True)
                # Add bottom banner
                embed2.set_image(url="https://i.imgur.com/i9s3LmJ.png")
                # Add copyright text as plain footer
                embed2.set_footer(text="Web Frens 2025 ©")

                view = discord.ui.View(timeout=None)
                view.add_item(
                    discord.ui.Button(label="Refresh Trends",
                                      style=discord.ButtonStyle.primary,
                                      custom_id="refresh_trends"))
                await interaction.response.edit_message(
                    embeds=[embed1, embed2], view=view)
                button_cooldowns[custom_id] = utcnow(
                )  # Update cooldown timestamp
            else:
                await interaction.response.edit_message(
                    content="❌ Couldn't fetch trends. Try again later.",
                    embeds=None,
                    view=None)
        except Exception as e:
            print(f"Error refreshing trends: {e}")
            await interaction.response.edit_message(
                content="❌ Error refreshing trends. Try again later.",
                embeds=None,
                view=None)


# Run the bot
token = os.getenv("DISCORD_BOT_TOKEN")
if token is None:
    raise ValueError("DISCORD_BOT_TOKEN environment variable is not set")
bot.run(token)