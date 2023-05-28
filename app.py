from flask import Flask,request
from solution import Solution

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        solver = Solution()
        data = request.form['data']
        try:
            result = solver.numDecodings(data)
            return str(result)
        except ValueError:
            return 'bad request', 400
    else:
        return "<html><head><title>This is Test App</title></head>" \
               "<body>" \
                "<h1>This is Test App</h1>"\
               "<form action='/' method=POST>" \
               "<input type='text' name='data' />" \
               "<input id='go' type='submit' />"\
               "</form>" \
               "</body></html>"


if __name__ == '__main__':
    app.run()
