from flask import Flask, render_template, request
from crawler import search_jobs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    jobs = []

    keyword = request.args.get('keyword', '')
    area = request.args.get('area', '')
    page = request.args.get('page', 1, type=int)

    if keyword or area:
        jobs = search_jobs(
            keyword=keyword,
            area=area,
            page=page
        )

    return render_template(
        'index.html',
        jobs=jobs,
        keyword=keyword,
        area=area,
        page=page
    )


if __name__ == '__main__':
    app.run(debug=True)
