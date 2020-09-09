import logging
from flask import Flask, request, jsonify, abort

from app.common import get_recipes, assert_fridge_is_valid, count_dishes

app = Flask('__main__')

logging.basicConfig(filename='app/log', level=logging.DEBUG)


@app.route('/', methods=['GET'])
def get_handler():
    return jsonify(get_recipes('app/cookbook.json'))


@app.route('/', methods=['POST'])
def post_handler():
    app.logger.info('Processing post request...')
    fridge = request.get_json()
    try:
        assert_fridge_is_valid(fridge)
    except TypeError:
        app.logger.error(f'Invalid fridge:{fridge}')
        abort(400)
    app.logger.info(f'Valid fridge:{fridge}')
    recipes = get_recipes('app/cookbook.json')
    dishes = count_dishes(recipes, fridge)
    app.logger.info(f'Returning dishes:{dishes}')
    return jsonify(dishes)


