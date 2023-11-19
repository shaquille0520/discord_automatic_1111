from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, render_template, request, jsonify
import discord
from discord.ext import commands
import time
import os
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
options = Options()
options.add_experimental_option("excludeSwitches",["enable-automation"])
app = Flask(__name__)
driver = webdriver.Chrome(options = options)
client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_message(message):
    message_content = message.content
    if message.author == client.user:
        exit()
    driver.get('http://127.0.0.1:7860/')
    while True:
        try:
            driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div/div/div[1]/div[2]/label/textarea").send_keys(message_content)
            driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/button[3]").click()
            time.sleep(1)
            prog=driver.find_element(By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div[3]/div[1]/div")
            break
        except:
            print('fucked up')
    while True:
        try:
            progtext=prog.text
            print(str(progtext))
        except StaleElementReferenceException:
            await message.channel.send(file=discord.File('C:\\Users\\mui\\Downloads\\pc link parser-20231114T022042Z-001\\second\\2023-11-18\\image.png'))
            print("done")

client.run('MTE3NTIyMDgwMDY2MDQzOTA1MA.Gut0nE.P_3fi1JjdNL1MHzHAVOQgQKi_Iju5NmzDN9G78')

