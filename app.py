import discord
import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

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
        await message.channel.send('Hello!')
        
client.run(os.getenv('TOKEN'))

@app.route('/')
def index():
    return 'BOTTY SERVER'

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()
