# Project 1: Discord-Bot  
  
# Research & Documentation  
  
## Setup  
  
- Once your bot has been created and is ready to be added to a guild, 
you must add it using the OAuth2 protocol through Discord's Developer Portal. 
In the Developer Portal, select "OAuth2" from the left-hand panel. Scroll down 
to the "SCOPES" options and select "bot". Then select desired options under 
the "BOT PERMISSIONS" options. This will cause Discord to generate an authorization URL for your application. Copy and paste this URL into the browser and select your desired guild from the dropdown box. Click "Authorize" and BOOM. Bot added.  
- To get an API Token, head back to the Developer Portal. Under the "TOKEN" section, click "Copy" to collect the API Token needed to get your bot up and running.  
- To use this API with the bot.py code, you'll need to add a new environment variable to the .env file. In the .env file, add new lines "DISCORD_TOKEN={your-bot's-token}" and "DISCORD_GUILD={your-guild's-name}". Replace the {} placeholders with your actual values. This will allow the bot.py code to pull these values from the .env file and get your bot going.  
- For the code to run properly, you'll have to install some packages onto your machine. First, you'll need to have Python3 installed. Then you can use pip to install the Python libraries you'll need.  
- One library you'll need is discord.py. This one implements Discord's APIs efficiently and includes Python's implementation of Async IO.  
- You'll also need the dotenv library. The bot.py file uses "load_dotenv()" to load environment variables from the .env file into the shell's environment variables to use with your code.  
  
  
## Usage  
  
- For my Discord Bot, you type "Levi!" into the server. Levi Ackerbot (don't judge me or my anime husbando) will then respond with one of Levi Ackerman's quotes from Attack on Titan. Practical? No. Entertaining? Yes.  
- We achieved this result by changing the bot.py code in a few ways. First, we took the formatting of the brooklyn_99_quotes example that already existed in the file and used it to set up or own form of quotes. In this case; levi_quotes. Then we added in as many Levi Ackerman quotes we wanted, keeping the format from the original example.  
- To make the bot respond with these quotes, we change the "if message.content == 'towel!':" line and replace "towel!" with "Levi!". Change the "response = random.choice(brooklyn_99_quotes)" line by replacing 'brooklyn_99_quotes" with levi)quotes".  
- Test your changes by running the bot.py code and typing "Levi!" into your Discord server. If you get a Levi quote; SUCCESS!  
- Here's some proof that our Levi Ackerbot worked:  
![Levi Ackerbot in action](https://github.com/WSU-kduncan/ceg3120-mhayslett16/blob/main/Discord-Bot/bot-proof.JPG)    
  
## Research  
  
- One solution to allow a bot to run 24/7 would be to use hosting services like Vultr, which has a low cost of $5 a month. There are more options that are evn less expensive. These work because they host your bot on one of their servers and keep the code running continuously.  
- Another solution is to use tools like node.js and PM2. PM2 would allow your code to continue running while your PC is on and you're signed in. Once you log off or shutdown, the bot will too.    
