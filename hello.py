"""This example demonstrates a basic API usage"""

from pyrogram import Client, Filters

# Create a new Client instance
app = Client("my_account")


@app.on_message(Filters.command("ping"))
def send_command(client, message):
     app.send_message(message.chat.id, msg.file_id, reply_to_message_id=msg.message_id)


app.run()