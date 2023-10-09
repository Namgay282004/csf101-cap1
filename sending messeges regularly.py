import pywhatkit
import time

# replace these with the recipient's number and the message to be sent
phone_number = "+975 77270847"
message = "Hello, this is a text through automation."

# replace these with the time you want your message to be delivered in hour and minute.
hours = 13  # 1-24
minutes = 33  # 0-59

while True:
    try:
        pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
        print("Message sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # wait for 24 hours before sending the next message
    time.sleep(24 * 60 * 60)
