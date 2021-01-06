import time, atexit
from apscheduler.schedulers.background import BackgroundScheduler
from app import app,\
                m_send

timer: int = 5 #86400 # 24 horas
should_send: bool = False


def check_send_event() -> None:
    """ Checks every 24 hours if should_send flag is True.
        If True it will send the email. If not, the `should_send` flag will be set to True.
        If flag is not changed in the next 24 hours, the email will then be sent.
    """
    global should_send

    if should_send != False:
        f = m_send()
        if f:
            print('# Email has been successfully sent ...')
        return
    
    should_send = True
    print(f'# Email will be sent if no cancel is being made in the next {timer} seconds')

    return


@app.route('/ping')
def handle_ping():
    global should_send
    should_send = False

    return should_send


sched = BackgroundScheduler(daemon=True)
sched.add_job(func=check_send_event, trigger="interval", seconds=timer)
sched.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: sched.shutdown())