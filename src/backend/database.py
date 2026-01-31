# Database Configuration for Manga Maniacs

from datetime import time

schedule = {
    'Manga Maniacs': {
        'schedule': 'Tuesdays, 5:00 PM - 6:00 PM',
        'schedule_details': {
            'start_time': time(17, 0),  
            'end_time': time(18, 0)
        },
        'max_participants': 25
        # Other configurations remain unchanged
    }
}