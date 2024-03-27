from aiogram import Dispatcher, F
from aiogram.filters import Command

from aiogram.types import Message

dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer('Привет! Этот бот поможет тебе получить инфомрацию об астрономических являенях!')