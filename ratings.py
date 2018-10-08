import sys

def restaurant_rating(file):
	"""Restaurant rating lister."""

	restaurant_ratings_dict = {}
	restaurant_ratings_list = []

	for scores in open(file):

		scores = scores.rstrip()
		scores = scores.split(':')
		restaurant_name = scores[0]
		rating = scores[1]
		
		restaurant_ratings_dict[restaurant_name] = rating
		


	for restaurant in restaurant_ratings_dict.items():
		restaurant_ratings_list.append(restaurant)

	restaurant_ratings_list = sorted(restaurant_ratings_list)
	#print (restaurant_ratings_list)

	for item in restaurant_ratings_list:
		print ('{} is rated at {}.'.format(item[0], item[1]))




	#print (restaurant_ratings_dict)

	


			


restaurant_rating(sys.argv[1])