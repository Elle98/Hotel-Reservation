from HotelReservation import  Booking
import empty
import datetime
class BookingTest:
    """
    Classe di test per la classe Booking.
    """
    def run_tests(self):
        # Test adding bookings
        hotel = Booking(2)
        """hotel.add_booking('Mario Rossi', 2, 'singola', '01/05/2023', '05/05/2023')
        hotel.add_booking('Luigi Verdi', 1, 'doppia', '02/05/2023', '04/05/2023')
    
        hotel.create_booking()"""

        print(hotel.available_rooms())

        print(hotel.reserved_rooms())

        hotel.add_booking('Mario Rossi', 2, 'singola', '01/05/2023', '05/05/2023')

        print(hotel.available_rooms())
        print(hotel.reserved_rooms())
        hotel.add_booking('Luigi Verdi', 1, 'doppia', '02/05/2023', '04/05/2023')
        print(hotel.available_rooms())
        print(hotel.reserved_rooms())
        






if __name__ == '__main__':
    booking_test = BookingTest()
    booking_test.run_tests()



