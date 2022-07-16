import requests
from tqdm import tqdm
import sys
from functools import wraps


def catch_connection_errors(function):
    """
    Decorator function checks for HTTP error and connection error of request sent to the API server
    :param function:
    :return: Wrapper function
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except requests.exceptions.HTTPError:
            print(f"Request Url not found.")
            sys.exit(1)
        except requests.exceptions.ConnectionError:
            print("No internet connection, please check your internet connection before continue.")
            sys.exit(1)
    return wrapper


@catch_connection_errors
def get_categories() -> dict:
    """
    Function gets quiz category from the public API
    :return: category dictionary in the format {id:category}
    """
    url = 'https://opentdb.com/api_category.php'
    progress = tqdm(range(1, 2))
    progress.set_description("Downloading quiz categories")
    response = None
    for _ in progress:
        response = requests.get(url)
        response.raise_for_status()
    return {category.get('id'): category.get('name') for category in response.json()['trivia_categories']}


@catch_connection_errors
def get_questions(amount: int, category: int) -> list:
    """
    function get questions from the public api with chosen amount and category
    :param amount:
    :param category:
    :return: list of questions
    """
    url = 'https://opentdb.com/api.php'
    params = {
        'amount': amount,
        'category': category
    }
    progress = tqdm(range(1, 2))
    progress.set_description("Downloading questions")
    response = None
    for _ in progress:
        response = requests.get(url=url, params=params)
        response.raise_for_status()
    return response.json()['results']


# testing function for the chosen API
if __name__ == '__main__':
    print(get_categories())
