import discord
import time
import os
from colorama import Fore, Style
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)

print(f"\n                                  {Fore.LIGHTCYAN_EX + Style.BRIGHT}Discord Mass DM Roles With Bot | {Fore.WHITE}[{Fore.LIGHTGREEN_EX}Albi{Fore.WHITE}]\n\n")

token = input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]  {Fore.YELLOW}Enter the bot token: ")

role_id = input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]  {Fore.YELLOW}Enter the role id you want to dm: ")
mass_dm = int(role_id)

message = input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]  {Fore.YELLOW}Enter the message you want to send: ")

sleep = input(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]  {Fore.YELLOW}Enter the time you want the bot to sleep inbetween dms (in seconds): ")
time_to_sleep = int(sleep)

async def send_dm(member, message):
    try:
        await member.send(message)
        print(f"{Fore.WHITE}[{Fore.LIGHTBLUE_EX}+{Fore.WHITE}]  {Fore.LIGHTBLUE_EX}Sent a dm to {Fore.WHITE}{member} ({member.id})")
    except discord.Forbidden:
        print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}-{Fore.WHITE}]  {Fore.LIGHTRED_EX}Couldn't send a dm to {Fore.WHITE}{member} ({member.id}){Fore.LIGHTRED_EX}. They have the bot blocked.")
        print(Style.RESET_ALL)

@client.event
async def on_ready():
    os.system("cls")
    print(f"\n                                  {Fore.LIGHTCYAN_EX + Style.BRIGHT}Discord Mass DM Roles With Bot | {Fore.WHITE}[{Fore.LIGHTGREEN_EX}Albi{Fore.WHITE}]\n\n")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}]  {Fore.LIGHTGREEN_EX}Logged in as {Fore.WHITE}{client.user} ({client.user.id})\n")
    print(Style.RESET_ALL)
    for guild in client.guilds:
        role = discord.utils.find(lambda r: r.id == mass_dm, guild.roles)
        for member in guild.members:
            if role in member.roles:
                await send_dm(member, message)
                await asyncio.sleep(time_to_sleep)
    print(f"----------------------------\n\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}]  {Fore.LIGHTGREEN_EX} Successfully messaged everyone with the role!")
    print(Style.RESET_ALL)
    input(f"----------------------------\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}]  {Fore.YELLOW}Press enter to exit the program.")
    quit()

client.run(token)
