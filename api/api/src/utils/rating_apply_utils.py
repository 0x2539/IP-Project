

def update_rating(tip_and_trick, rating, old_rating):
    number_of_ratings = tip_and_trick.number_of_ratings

    tip_and_trick.average_rating = (tip_and_trick.average_rating * number_of_ratings - old_rating + rating) / number_of_ratings

    return tip_and_trick


def add_rating(tip_and_trick, rating):
    number_of_ratings = tip_and_trick.number_of_ratings

    tip_and_trick.number_of_ratings = number_of_ratings + 1
    tip_and_trick.average_rating = (tip_and_trick.average_rating * number_of_ratings + rating) / (number_of_ratings + 1)

    return tip_and_trick
