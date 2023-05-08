from datetime import datetime
from queue1 import ArrayQueue, Empty
from hash_map_base import HashMapBase




class Booking:
    """
    Rappresenta una prenotazione in un hotel.
    """

    def __init__(self, num_rooms):
        """
        Crea una nuova prenotazione con i dati specificati.
        """
        self._name = None
        self._num_rooms = num_rooms
        self._room_type = None
        self._check_in_date = None
        self._check_out_date = None
        self._bookings = ArrayQueue()
        #self.ricerca = HashMapBase()


    def get_name(self):
        """
        Restituisce il nome del cliente che ha effettuato la prenotazione.
        """
        return self._name

    def get_room_type(self):
        """
        Restituisce il tipo di camera prenotata.
        """
        return self._room_type

    def get_check_in_date(self):
        """
        Restituisce la data di check-in della prenotazione.
        """
        return self._check_in_date

    def get_check_out_date(self):
        """
        Restituisce la data di check-out della prenotazione.
        """
        return self._check_out_date

    def cancel_room(self):
        """
        Annulla la prenotazione di una camera nell'hotel.

        Solleva l'eccezione Empty se non ci sono camere prenotate.
        """
        if self._bookings.is_empty():
            raise Empty('Nessuna camera prenotata')
        self._bookings.dequeue()

    def add_booking(self, name, num_rooms, room_type, check_in_date, check_out_date):
        """
        Aggiunge una nuova prenotazione alla coda FIFO.

        :param check_out_date: la data di check-out della prenotazione, nel formato 'dd/mm/yyyy'.
        :param check_in_date: la data di check-in della prenotazione, nel formato 'dd/mm/yyyy'.
        :param room_type:
        :param num_rooms:
        :param name: il nome dell'ospite che effettua la prenotazione.

        """
        checkin = datetime.strptime(check_in_date, '%d/%m/%Y')
        checkout = datetime.strptime(check_out_date, '%d/%m/%Y')
        if checkin >= checkout:
            raise ValueError('La data di check-in deve precedere la data di check-out')
        if len(self._bookings) < self._num_rooms:
            booking = {'name': name, "num_rooms": num_rooms, "room_type": room_type, 'checkin': checkin, 'checkout': checkout}
            self._bookings.enqueue(booking)
            print(f"Prenotazione aggiunta per {name}")
        else:
            print(f"Mi dispiace, non ci sono camere disponibili per {name}")

    def create_booking(self):
        """
        Crea una nuova prenotazione a partire dalla testa della coda FIFO.

        :return: un dizionario contenente i dettagli della prenotazione (nome dell'ospite, data di check-in e data di check-out).
        """
        if self._bookings.is_empty():
            raise Empty('La coda delle prenotazioni è vuota')
        booking = self._bookings.first()
        name = booking['name']
        num_rooms = booking['num_rooms']
        room_type = booking['room_type']
        checkin = booking['checkin']
        checkout = booking['checkout']
        self._bookings.dequeue()
        return {'name': name, 'num_rooms': num_rooms, 'room_type': room_type, 'checkin_date': checkin.strftime('%d/%m/%Y'),
                'checkout_date': checkout.strftime('%d/%m/%Y')}

    def available_rooms(self):
        num_bookings = len(self._bookings)
        num_available = self._num_rooms - num_bookings
        return num_available

    def reserved_rooms(self):
        """
        Restituisce il numero di camere prenotate nell'hotel.

        """
        return len(self._bookings)

    def find_booking(self, name):

        """
        Cerca la prenotazione associata al cliente con il nome specificato e restituisce i dettagli della prenotazione.
        Solleva l'eccezione KeyError se non esiste nessuna prenotazione associata al nome del cliente.
        """
        try:
            booking = self.ricerca.__getitem__(name)
        except KeyError:
            raise KeyError(f"Prenotazione non trovata per il cliente '{name}'")

        return f"Cliente: {booking.client_name}, Data: {booking.date}, Ora: {booking.time}"
