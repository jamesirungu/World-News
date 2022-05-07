from flask import render_template, request, redirect, url_for
from . import main
from ..request import getHeadlines, getSources


@main.route('/')
def index():
    us_headlines = getHeadlines('us')
    uk_headlines = getHeadlines('gb')
    german_headlines = getHeadlines('de')
    sa_headlines = getHeadlines('sa')
    china_headlines = getHeadlines('cn')
    russia_headlines = getHeadlines('rs')

    title = 'Country Headlines'
    return render_template('index.html', title=title, us_headlines=us_headlines,
                           uk_headlines=uk_headlines, german_headlines=german_headlines,
                           sa_headlines=sa_headlines, china_headlines=china_headlines,
                           russia_headlines=russia_headlines)
