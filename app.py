from flask import Flask, render_template, request
from crawler import search_jobs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    jobs = []
    total_pages = 0
    keyword = request.args.get('keyword', '')
    areas = request.args.getlist('area')
    area = ','.join(areas)
    page = request.args.get('page', 1, type=int)

    if keyword or area:
        jobs, total_pages = search_jobs(
            keyword=keyword,
            area=area,
            page=page
        )

    return render_template(
        'index.html',
        jobs=jobs,
        keyword=keyword,
        area=area,
        page=page,
        areas=areas,
        total_pages=total_pages
    )


if __name__ == '__main__':
    app.run(debug=True)
