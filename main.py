import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
from dotenv import load_dotenv
import logging
from models import Base, Attendance, Break, WorkTime, SpamControl, ServerConfig
from database import get_engine, get_session_factory, init_db
from services.auto_warning_service import AutoWarningService

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class AttendanceBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="/",
            intents=intents,
            application_id=int(os.getenv('APPLICATION_ID', 0))
        )
        self.initial_extensions = [
            'cogs.attendance',
            'cogs.work_time',
            'cogs.offline_monitor',
            'cogs.admin',
            'cogs.help_command',
            'cogs.reports',
            'cogs.spam_control',
            'cogs.dm_control',
            'cogs.manual_attendance',
            'cogs.dayoff_manager'
        ]
        self.auto_warning_service = None

    async def setup_hook(self):
        for ext in self.initial_extensions:
            try:
                await self.load_extension(ext)
                logger.info(f"Loaded extension: {ext}")
            except Exception as e:
                logger.error(f"Failed to load extension {ext}: {e}")
        
        # Khởi tạo auto warning service
        self.auto_warning_service = AutoWarningService(self)
        logger.info("Auto warning service initialized")

    async def on_ready(self):
        if self.user:
            logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
            logger.info("Syncing commands...")
            await self.tree.sync()
            logger.info("Commands synced!")
            
            # Bắt đầu monitoring
            if self.auto_warning_service:
                self.auto_warning_service.start_monitoring()
                logger.info("Auto warning monitoring started!")
                logger.info(f"  - Check-in grace period: {self.auto_warning_service.CHECKIN_GRACE_MINUTES} minutes")
                logger.info(f"  - Check-out grace period: {self.auto_warning_service.CHECKOUT_GRACE_MINUTES} minutes")
            
            logger.info("------")
        else:
            logger.info("Logged in but user is not initialized")
            logger.info("------")
    
    async def on_command_error(self, ctx, error):
        """Suppress CommandNotFound errors since we only use slash commands"""
        if isinstance(error, commands.CommandNotFound):
            # Silently ignore - user is trying to use prefix commands
            # All commands are slash commands, use / instead of !
            return
        # Log other errors
        logger.error(f"Command error: {error}")

# Create bot instance
bot = AttendanceBot()

if __name__ == "__main__":
    # Run the bot
    token = os.getenv('DISCORD_TOKEN')
    if token:
        bot.run(token)
    else:
        logger.error("No token provided. Please set the DISCORD_TOKEN environment variable.")