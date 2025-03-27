import unittest
from datetime import date
from hotel import Hotel
from room import Room
from guest import Guest
from booking import Booking
from payment import Payment


class TestHotelManagement(unittest.TestCase):
    def setUp(self):
        """Initialize sample data for Abu Dhabi hotels and Arabic guest names."""
        self.hotel = Hotel("Emirates Palace Abu Dhabi")
        self.hotel2 = Hotel("The St. Regis Abu Dhabi")

        self.room1 = Room(101, "Deluxe", 500, True)
        self.room2 = Room(102, "Suite", 1000, True)
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)

        self.guest1 = Guest("Fatima", "fatima@example.com", "0501234567", False)
        self.guest2 = Guest("Ahmed", "ahmed@example.com", "0507654321", True)

    def test_guest_creation(self):
        """Test guest account creation and data storage."""
        self.assertEqual(self.guest1.name, "Fatima")
        self.assertEqual(self.guest1.email, "fatima@example.com")
        self.assertFalse(self.guest1.is_loyal)

        self.assertEqual(self.guest2.name, "Ahmed")
        self.assertTrue(self.guest2.is_loyal)

    def test_search_available_rooms(self):
        """Test searching for available rooms by criteria."""
        available_rooms = self.hotel.search_available_rooms("Deluxe")
        self.assertIn(self.room1, available_rooms)

        available_rooms_suite = self.hotel.search_available_rooms("Suite")
        self.assertIn(self.room2, available_rooms_suite)

    def test_make_room_reservation(self):
        """Test making a room reservation."""
        booking1 = Booking(self.guest1, self.room1, date(2024, 5, 1), date(2024, 5, 5))
        booking2 = Booking(self.guest2, self.room2, date(2024, 6, 1), date(2024, 6, 3))

        self.assertEqual(booking1.guest.name, "Fatima")
        self.assertEqual(booking2.room.room_type, "Suite")

    def test_booking_confirmation_notification(self):
        """Test that a confirmation message is sent upon booking."""
        booking = Booking(self.guest1, self.room1, date(2024, 5, 1), date(2024, 5, 5))
        confirmation = booking.send_confirmation()
        self.assertIn("Booking confirmed", confirmation)

    def test_invoice_generation(self):
        """Test invoice generation upon booking completion."""
        booking = Booking(self.guest1, self.room1, date(2024, 5, 1), date(2024, 5, 5))
        invoice = booking.generate_invoice()
        self.assertIn("Total Amount", invoice)

    def test_payment_processing(self):
        """Test processing payments with different methods."""
        payment1 = Payment(self.guest1, 2000, "Credit Card")
        payment2 = Payment(self.guest2, 3000, "Mobile Wallet")

        self.assertEqual(payment1.payment_method, "Credit Card")
        self.assertEqual(payment2.amount, 3000)

    def test_reservation_history(self):
        """Test displaying a guest’s past reservations."""
        self.guest1.add_booking("Emirates Palace", "Deluxe", date(2023, 5, 1), date(2023, 5, 5))
        self.guest1.add_booking("The St. Regis Abu Dhabi", "Suite", date(2024, 1, 10), date(2024, 1, 15))

        self.assertEqual(len(self.guest1.bookings), 2)

    def test_cancel_reservation(self):
        """Test reservation cancellation and room availability update."""
        booking = Booking(self.guest1, self.room1, date(2024, 5, 1), date(2024, 5, 5))
        cancellation_message = booking.cancel()
        self.assertIn("canceled", cancellation_message)


if __name__ == "__main__":
    unittest.main()
