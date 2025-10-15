import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from cogs.attendance import Attendance
from cogs.work_time import WorkTime
from cogs.spam_control import SpamControl
from cogs.offline_monitor import OfflineMonitor
from cogs.dm_control import DMControl
from cogs.admin import Admin

# Load environment variables
load_dotenv()

# Initialize bot with required intents
class HRBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        intents.presences = True  # For monitoring online/offline status
        super().__init__(command_prefix='!', intents=intents)
        
        # Store last message times for spam control
        self.last_messages = {}
        # Store offline start times
        self.offline_starts = {}
        
    async def setup_hook(self):
        # Add cogs
        await self.add_cog(Attendance(self))
        await self.add_cog(WorkTime(self))
        await self.add_cog(SpamControl(self))
        await self.add_cog(OfflineMonitor(self))
        await self.add_cog(DMControl(self))
        await self.add_cog(Admin(self))
        
        # Start background tasks
        self.check_offline_status.start()
        self.check_long_breaks.start()
        
        # Sync commands with Discord
        await self.tree.sync()
        
    async def on_ready(self):
        if self.user:
            print(f'Logged in as: {self.user.name}')
            print('------')
        else:
            print('Logged in but user is not initialized')
            print('------')
        
    async def on_message(self, message):
        # Ignore bot messages
        if message.author.bot:
            return
            
        # Check for spam
        await self.check_spam(message)
        
        # Check for DMs between members
        if isinstance(message.channel, discord.DMChannel):
            await self.check_dm(message)
            
        await self.process_commands(message)
        
    async def check_spam(self, message):
        user_id = str(message.author.id)
        channel_id = str(message.channel.id)
        now = datetime.now()
        
        # Get user's last messages
        key = f"{user_id}:{channel_id}"
        if key not in self.last_messages:
            self.last_messages[key] = []
            
        # Add new message time
        self.last_messages[key].append(now)
        
        # Remove messages older than 5 seconds
        self.last_messages[key] = [
            t for t in self.last_messages[key]
            if (now - t).total_seconds() <= 5
        ]
        
        # Check if spamming (more than 5 messages in 5 seconds)
        if len(self.last_messages[key]) > 5:
            # Warn or mute user
            await self.handle_spam(message.author, message.channel)
            
    async def handle_spam(self, member, channel):
        # TODO: Implement spam handling (warning, muting, etc)
        pass
        
    async def check_dm(self, message):
        # TODO: Implement DM control
        pass
        
    @tasks.loop(minutes=1)
    async def check_offline_status(self):
        """Check for members who have been offline for too long"""
        now = datetime.now()
        for guild in self.guilds:
            for member in guild.members:
                if not member.bot:
                    status = str(member.status)
                    user_id = str(member.id)
                    
                    if status == "offline":
                        if user_id not in self.offline_starts:
                            self.offline_starts[user_id] = now
                        elif (now - self.offline_starts[user_id]).total_seconds() > 300:  # 5 minutes
                            await self.report_offline(member)
                    else:
                        if user_id in self.offline_starts:
                            del self.offline_starts[user_id]
                            
    async def report_offline(self, member):
        # TODO: Implement offline reporting
        pass
        
    @tasks.loop(minutes=1)
    async def check_long_breaks(self):
        """Check for breaks that have exceeded the maximum time"""
        # TODO: Implement break time monitoring
        pass

# Create and run bot
if __name__ == '__main__':
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN not found in environment variables")
        exit(1)
        
    bot = HRBot()
    bot.run(token)