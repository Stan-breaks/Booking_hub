from __future__ import print_function
import africastalking
import requests
from flask import Flask, request

# url = "https://localhost:8000/ussd"
app = Flask(__name__)
# user_name = requests.get(url + "/user").text
user_name = "John Doe"


@app.route("/ussd", methods=["POST"])
def ussd():
    # Read the variables sent via POST from our API

    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == "":
        # This is the first request.
        response = (
            "CON Welcome to Booking hub, {} \n".format(user_name)
            + "What would you like to book today?\n"
        )

        response += "1. Travel Booking \n"
        response += "2. Hotel Booking \n"
        response += "3. Car Rental \n"
        response += "4. Event Tickets \n"

    elif text == "1":
        # Travel Booking
        response = "CON You chose travel \n"
        response += "Please press 1. to continue\n"

    elif text == "1*1":
        response = "CON The travel companies are \n"
        response += "1. Expedia \n"
        response += "2. Travelocity \n"
        response += "3. Orbitz \n"

    elif text == "1*1*1":
        response = "CON Thank you for choosing Expedia.\n You can either :\n"
        response += "1. Book flights \n"
        response += "2. Book hotels \n"
        response += "3. Book packages \n"

    elif text == "1*1*1*1":
        response = "CON Enter your travel details:\n"
        response += "1. One-way flight \n"
        response += "2. Round-trip flight \n"
        response += "3. Multi-city flight \n"

    elif text == "1*1*1*1*1":
        response = "CON Enter departure city, destination city, and travel date (e.g., New York, Los Angeles, 2024-06-15)"
    elif text.startswith("1*1*1*1*1*"):
        flight_details = text.split("*")[5].split(",")
        departure_city = flight_details[0]
        destination_city = flight_details[1]
        travel_date = flight_details[2]

        response = "END Your flight details have been received. You will receive a confirmation shortly."

        # Send flight details to the user via SMS
        sms_message = f"Your one-way flight from {departure_city} to {destination_city} on {travel_date} has been confirmed. Thank you for using Expedia."
        SMS().send(sms_message, [phone_number])  # Add more options for Expedia flights
        return response
    elif text == "1*1*1*2":
        response = "CON Enter your hotel details:\n"
        response += "1. City or location \n"
        response += "2. Check-in and check-out dates \n"
        response += "3. Number of rooms and guests \n"

    # Add more options for Expedia hotels

    elif text == "1*1*1*3":
        response = "CON Enter your package details:\n"
        response += "1. Destination \n"
        response += "2. Travel dates \n"
        response += "3. Number of travelers \n"

    # Add more options for Expedia packages

    elif text == "2":
        # Hotel Booking
        response = "CON These are the hotel booking companies\n"
        response += "1. Booking.com \n"
        response += "2. Hotels.com \n"
        response += "3. Agoda \n"

    elif text == "2*1":
        response = "CON Thank you for choosing Booking.com.\n"
        response += "1. Search for hotels \n"
        response += "2. View your bookings \n"
        response += "3. Cancel a booking \n"

    elif text == "2*1*1":
        response = "CON Enter your hotel search criteria:\n"
        response += "1. City or location \n"
        response += "2. Check-in and check-out dates \n"
        response += "3. Number of rooms and guests \n"

    # Add more options for Booking.com hotel search

    elif text == "2*1*2":
        response = "CON Enter your booking reference number"

    elif text == "2*1*2*ABC123":
        response = (
            "END Your booking details have been retrieved and sent to you via SMS."
        )
        # Send booking details to the user via SMS
        SMS().send(
            "Your booking at the Hilton Hotel has been confirmed. Thank you for using Booking.com.",
            [phone_number],
        )
    # Add more options for viewing and canceling bookings

    elif text == "3":
        # Car Rental
        response = "CON These are the car rental companies\n"
        response += "1. Hertz \n"
        response += "2. Avis \n"
        response += "3. Enterprise \n"

    elif text == "3*1":
        response = "CON Thank you for choosing Hertz.\n"
        response += "1. Rent a car \n"
        response += "2. View or modify reservation \n"
        response += "3. Check rental rates \n"

    elif text == "3*1*1":
        response = "CON Enter your rental details:\n"
        response += "1. Pick-up location \n"
        response += "2. Pick-up and drop-off dates \n"
        response += "3. Car type \n"

    # Add more options for Hertz car rental

    elif text == "3*1*2":
        response = "CON Enter your reservation number"

    elif text == "3*1*2*XYZ456":
        response = (
            "END Your reservation details have been retrieved and sent to you via SMS."
        )
        # Send reservation details to the user via SMS
        SMS().send(
            "Your reservation for a compact car at Hertz has been confirmed. Thank you for using Hertz.",
            [phone_number],
        )

    # Add more options for viewing and modifying reservations

    elif text == "4":
        # Event Tickets
        response = "CON These are the event ticketing companies\n"
        response += "1. Ticketmaster \n"
        response += "2. LiveNation \n"
        response += "3. AXS \n"

    elif text == "4*1":
        response = "CON Thank you for choosing Ticketmaster.\n"
        response += "1. Search for events \n"
        response += "2. View your orders \n"
        response += "3. Sell tickets \n"

    elif text == "4*1*1":
        response = "CON Enter your event search criteria:\n"
        response += "1. Event type (e.g., concert, sports, theater) \n"
        response += "2. Location \n"
        response += "3. Date or date range \n"

    # Add more options for Ticketmaster event search

    elif text == "4*1*2":
        response = "CON Enter your order number"

    elif text == "4*1*2*789012":
        response = "END Your order details have been retrieved and sent to you via SMS."
        SMS().send(
            "Your order of 2 tickets for the concert on 2024-06-15 has been confirmed. Thank you for using Ticketmaster.",
            [phone_number],
        )

    # Add more options for viewing orders and selling tickets

    else:
        response = "END Invalid choice"

    # Send SMS if needed
    if response.startswith("END"):
        SMS().send(response.split("END ")[1], [phone_number])
    else:
        return response


# works with both python 2 and 3


class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = "app001"
        self.api_key = (
            "ae4ab7920eb757987e814f0360fa12ae8e3bafa3220ddc46968e73d5ad680754"
        )

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, mess, recipients):
        # Set the numbers you want to send to in international format

        # Set your message
        message = mess

        # Set your shortCode or senderId
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print("Encountered an error while sending: %s" % str(e))


if __name__ == "__main__":
    app.run(debug=True)
