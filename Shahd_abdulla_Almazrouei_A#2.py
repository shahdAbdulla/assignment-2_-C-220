from datetime import date


# Class 1: Hotel (Composition with Room)
class Hotel:
    def __init__(self, name: str, location: str, total_rooms: int):
        """Initializes a Hotel with a name, location, and a list of rooms."""
        self.__name = name
        self.__location = location
        self.__total_rooms = total_rooms
        self.__rooms = []  # Composition: Hotel owns Rooms

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_location(self):
        return self.__location

    def set_location(self, location: str):
        self.__location = location

    def get_total_rooms(self):
        return self.__total_rooms

    def set_total_rooms(self, total_rooms: int):
        self.__total_rooms = total_rooms

    def add_room(self, room):
        """Adds a Room to the hotel."""
        self.__rooms.append(room)

    def remove_room(self, room):
        """Removes a Room from the hotel."""
        self.__rooms.remove(room)

    def __str__(self):
        return f"Hotel {self.__name} located in {self.__location} with {self.__total_rooms} rooms."


# Class 2: Room (Used in Hotel - Composition)
class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: float, is_available: bool):
        self.__room_number = room_number
        self.__type = room_type
        self.__amenities = []
        self.__price_per_night = price_per_night
        self.__is_available = is_available

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number: int):
        self.__room_number = room_number

    def get_type(self):
        return self.__type

    def set_type(self, room_type: str):
        self.__type = room_type

    def get_amenities(self):
        return self.__amenities

    def set_amenities(self, amenities: list):
        self.__amenities = amenities

    def get_price_per_night(self):
        return self.__price_per_night

    def set_price_per_night(self, price: float):
        self.__price_per_night = price

    def is_room_available(self):
        return self.__is_available

    def set_availability(self, status: bool):
        self.__is_available = status

    def book_room(self):
        if self.__is_available:
            self.__is_available = False

    def checkout(self):
        self.__is_available = True

    def __str__(self):
        return f"Room {self.__room_number} ({self.__type}) - ${self.__price_per_night} per night. Available: {self.__is_available}"


# Class 3: Guest
class Guest:
    def __init__(self, name: str, contact_info: str, email: str, phone_number: str):
        self.__name = name
        self.__contact_info = contact_info
        self.__email = email
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info: str):
        self.__contact_info = contact_info

    def get_email(self):
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def create_account(self):
        pass  # Future implementation

    def view_history(self):
        pass  # Future implementation

    def __str__(self):
        return f"Guest: {self.__name}, Contact: {self.__contact_info}, Email: {self.__email}, Phone: {self.__phone_number}"


# Class 6: LoyalGuest (Inheritance from Guest)
class LoyalGuest(Guest):
    def __init__(self, name, contact_info, email, phone_number, points_earned: int, membership_level: str):
        super().__init__(name, contact_info, email, phone_number)
        self.__points_earned = points_earned
        self.__membership_level = membership_level

    def get_points_earned(self):
        return self.__points_earned

    def set_points_earned(self, points: int):
        self.__points_earned = points

    def get_membership_level(self):
        return self.__membership_level

    def set_membership_level(self, level: str):
        self.__membership_level = level

    def redeem_points(self):
        pass  # Future implementation

    def __str__(self):
        return f"Loyal Guest: {self.get_name()}, Membership: {self.__membership_level}, Points: {self.__points_earned}"

# booking.py (Class 4: Booking)
from datetime import date
from guest import Guest
from room import Room

class Booking:
    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in_date: date, check_out_date: date, total_price: float):
        self.__booking_id = booking_id
        self.__guest = guest  # Aggregation (Guest exists independently)
        self.__room = room  # Association with Room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__total_price = total_price

    def get_booking_id(self):
        return self.__booking_id

    def get_guest(self):
        return self.__guest

    def get_room(self):
        return self.__room

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_total_price(self):
        return self.__total_price

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def confirm_booking(self):
        self.__room.set_availability(False)  # Mark room as booked

    def cancel_booking(self):
        self.__room.set_availability(True)  # Make room available again


# payment.py (Class 5: Payment)
from booking import Booking

class Payment:
    def __init__(self, payment_id: int, booking: Booking, amount: float, method: str):
        self.__payment_id = payment_id
        self.__booking = booking  # Association with Booking
        self.__amount = amount
        self.__method = method

    def get_payment_id(self):
        return self.__payment_id

    def get_booking(self):
        return self.__booking

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_method(self):
        return self.__method

    def set_method(self, method):
        self.__method = method

    def process_payment(self):
        return f"Payment of {self.__amount} via {self.__method} processed successfully."


# loyalty_program.py (Class 7: LoyaltyProgram)
class LoyaltyProgram:
    def __init__(self, points_earned: int, rewards: list):
        self.__points_earned = points_earned
        self.__rewards = rewards

    def get_points_earned(self):
        return self.__points_earned

    def set_points_earned(self, points):
        self.__points_earned = points

    def get_rewards(self):
        return self.__rewards

    def set_rewards(self, rewards):
        self.__rewards = rewards

    def redeem_points(self):
        if self.__points_earned >= 100:
            self.__points_earned -= 100
            return "Reward redeemed!"
        return "Not enough points to redeem."


# service_request.py (Class 8: ServiceRequest)
from guest import Guest

class ServiceRequest:
    def __init__(self, request_id: int, guest: Guest, request_type: str, status: str):
        self.__request_id = request_id
        self.__guest = guest  # Association with Guest
        self.__type = request_type
        self.__status = status

    def get_request_id(self):
        return self.__request_id

    def get_guest(self):
        return self.__guest

    def get_type(self):
        return self.__type

    def set_type(self, request_type):
        self.__type = request_type

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def submit_request(self):
        return f"Service request '{self.__type}' submitted. Status: {self.__status}."


# feedback.py (Class 9: Feedback)
from guest import Guest

class Feedback:
    def __init__(self, feedback_id: int, guest: Guest, rating: int, comments: str):
        self.__feedback_id = feedback_id
        self.__guest = guest  # Association with Guest
        self.__rating = rating
        self.__comments = comments

    def get_feedback_id(self):
        return self.__feedback_id

    def get_guest(self):
        return self.__guest

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_comments(self):
        return self.__comments

    def set_comments(self, comments):
        self.__comments = comments

    def submit_feedback(self):
        return f"Feedback submitted. Rating: {self.__rating}, Comments: {self.__comments}"

