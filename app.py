from app import app

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True;
    app.run()
