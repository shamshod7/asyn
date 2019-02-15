from pyrogram import Client, Emoji, Filters

"""
This is the Welcome Bot in @PyrogramChat
It uses the Emoji module to easily add emojis in your text messages and Filters
to make it only work for specific messages in a specific chat 
"""

app = Client("my_account")


@app.on_message(Filters.chat("Qopqon") & Filters.new_chat_members)
def welcome(client, message):
    file_id = "https://media.giphy.com/media/OF0yOAufcWLfi/giphy.gif"
    app.send_document(
        message.chat.id, file_id,
        reply_to_message_id=message.message_id
    )


app.start()
app.idle()