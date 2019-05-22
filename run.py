from app.recommender import Recommender
import click


@click.command('recommend')
@click.argument('path')
def recommend(path):
    r = Recommender(path)
    recommendations = r.get()
    print(recommendations)


if __name__ == "__main__":
    recommend()