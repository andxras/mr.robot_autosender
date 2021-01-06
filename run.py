from app import app

if __name__=='__main__':
    # init web server
    app.run('0.0.0.0', port=5000)