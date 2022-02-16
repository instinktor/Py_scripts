import asyncio
import json
import socketio
from discord.ext import commands

TOKEN = #Ваш токен DA в ''
TOKEN_bot = #Ваш токен ДисБота в ''
bot = commands.Bot(command_prefix='!')
sio = socketio.Client()

@sio.on('connect')
def on_connect():
	sio.emit('add-user', {"token": TOKEN, "type": "alert_widget"})
@sio.on('donation')

def on_message(data):
	y = json.loads(data)
	text = "New donate from: " + (y['username']), (y['amount']), (y['currency'])
	channel = #your-channel-id
	asyncio.run_coroutine_threadsafe(send_msg(channel, text), bot.loop)

async def send_msg(channel, text):
	channel = bot.get_channel(channel)
	await channel.send(text)
print ("Что, кожанный мешок, Бота запустил, Бабок ждешь.... ну ну.... ну давай подождем.... ")
sio.connect('wss://socket.donationalerts.ru:443',transports='websocket')
bot.run(TOKEN_bot)
