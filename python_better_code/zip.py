names = ["Vijay","Surya","Kamal"]
heroes = ["Leo","Rolex","Vikram"]
total_movies = [67,55,70]

# The code is using the `zip()` function to iterate over three lists simultaneously: `names`,
# `heroes`, and `total_movies`.
for name, hero, universe in zip(names,heroes,total_movies):
    print(f'{name} is actually {hero} from {universe}')