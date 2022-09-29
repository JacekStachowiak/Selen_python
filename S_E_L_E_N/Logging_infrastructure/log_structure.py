'''
Logging Demo 1 - czas, info
Logging Levels - rozróżniamy działania aplikacji
DEBUG - info, błędy przy debugowaniu, diagnozujemy problemy
INFO - potwierdzenie że działa OK
WARNING - nieoczekiwane zdarzenie, ostrzeżenie - ale oprogramowanie nadal działa
ERROR - stało się coś poważnego
CRITICAL - sam program nie będzie działać
'''
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://docs.python.org/3/library/time.html#strftime


import logging

# logging.warning('warning message')
# logging.info('info message') # nie drukuje - domyślnie usyawienie powyżej warning
# Clogging.error('error message')
# logging.critical('critical message')

# do pliku test.log                                                                                     %I-12 godz %a-am, pm
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', filename='test.log', datefmt='%Y/%m/%d %H:%M %p', level=logging.DEBUG)
logging.warning("warning message")
logging.info('info message')
logging.error("error message")
logging.critical('critical message')


