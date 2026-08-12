from flask import Flask, render_template, request
from crawler import search_jobs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    jobs = []

    if request.method == 'POST':

        keyword = request.form.get('keyword')
        area = request.form.get('area')

        jobs = search_jobs(
            keyword=keyword,
            area=area
        )

    return render_template(
        'index.html',
        jobs=jobs
    )


if __name__ == '__main__':
    app.run(debug=True)
