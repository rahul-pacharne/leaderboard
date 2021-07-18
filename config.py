import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    L1 = ['Is Australia the largest producer of wool in the world?','Do camels have three sets of eyelids?','Is China the largest country in the world?', 'Is Venus the closest planet to the Sun?', ' Spiders have 6 legs. Is it true or false?']
    A1 = ['T','T', 'F','F','F']


    L2 = ['The minimum time taken by a sloth to digest food is 2 weeks.','World War I took place on 28th July 1945.','Is it possible to sneeze while asleep?', 'Watching horror movies doesn’t cause any reaction in your body.', 'Zeus is known as the king of Gods.']

    A2 = ['T', 'F', 'F', 'F','T']



    L3 = ['Every 7 days, a new layer of epidermis appears on your skin.', 'Bats always turn left when they are exiting the caves. True or false?', 'A slug has four noses in total.', 'You won’t find any hair on a rhinoceros’ nose.','Honeybees are the fastest flying insect.']
    A3 = ['F','F','T','F', 'F']


    L4 = ['Australia is both a country and a continent.', 'Do shrimps have a unique feature, where their heart can be found in their head?', 'The highest number of shopping malls can be found in New Jersey.', 'There is no railway system in Iceland.', 'Meat is consumed by herbivore animals.']
    A4 = ['T', 'T', 'T', 'T', 'F']


    L5 = ['The longest and strongest bone in the human body is the thighbone.', 'Humans have 4 senses.', 'There are 184 countries in the world.','Archimedes is considered as the father of History.', 'It is normal to lose a minimum of 50-100 strands a day from your scalp, no matter how healthy it is.']
    A5 = ['T', 'F', 'F','F','T']


    L6 = ['A group of crows is called a ‘murder’.','you need oxygen for breathing', 'The full form of CVD is cardiovascular disease?', 'An increase in RBCs has nothing to do with the onset of anaemia.', 'Robert Brown discovered the cell nucleus']
    A6 = ['T', 'T', 'T', 'T', 'T']
