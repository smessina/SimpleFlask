from flask import Flask, request

app = Flask(__name__, static_url_path = '', static_folder = 'public')

@app.route('/')
@app.route('/*')
def static_file() :
    file = "index.html" if request.path == "/" else request.path

    return app.send_static_file( file )

if __name__ == '__main__' :
    app.run()
