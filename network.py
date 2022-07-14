import requests


def get_categories() -> dict:
    url = 'https://opentdb.com/api_category.php'
    response = requests.get(url)
    response.raise_for_status()
    return {category.get('id'): category.get('name') for category in response.json()['trivia_categories']}


def get_questions(amount: int, category: int) -> list:
    params = {
        'amount': amount,
        'category': category
    }
    response = requests.get(url='https://opentdb.com/api.php', params=params)
    response.raise_for_status()
    return response.json()['results']


if __name__ == '__main__':
    print(get_categories())
    print(get_questions(10, 18))
