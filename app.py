import discord
import os
import threading
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/')
def index():
    return 'BOTTY SERVER'

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('hi')

def start_discord_bot():
    client.run(os.getenv('TOKEN'))

if __name__ == '__main__':
    discord_thread = threading.Thread(target=start_discord_bot)
    discord_thread.start()
    app.run()
