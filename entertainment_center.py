import movies
import fresh_tomatoes
toy_story= movies.Movie("Toy Story","Set in a world where toys are shown to be living things who pretend to be lifeless when their owners are present, the film focus on the toys of a six-year-old boy Andy Davis"
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://www.youtube.com/watch?v=v2AVYvfNGfg")
finding_dory= movies.Movie("Finding Dory","One year after the events of Finding Nemo, Dory, a regal blue tang, experiences dreams of her life prior to meeting Marlin and Nemo, particularly about her parents."
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg","https://www.youtube.com/watch?v=3JNLwlcPBPI")
finding_nemo= movies.Movie("Finding Nemo","Two ocellaris clownfish, Marlin and his wife Coral, admire their new home in the Great Barrier Reef and their clutch of eggs when a barracuda attacks, knocking Marlin unconscious. He wakes up to find out that Coral and all but one of the eggs have been eaten by the barracuda. Marlin names this last egg Nemo, a name that Coral liked."
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/2/29/Finding_Nemo.jpg/220px-Finding_Nemo.jpg","https://www.youtube.com/watch?v=wZdpNglLbt8")
attack_on_titan= movies.Movie("Attack on Titan","The story of Attack on Titan revolves around the adventures of Eren Yeager, his foster sister, Mikasa Ackerman, and their childhood friend Armin Arlert."
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Shingeki_no_Kyojin_manga_volume_1.jpg/220px-Shingeki_no_Kyojin_manga_volume_1.jpg","https://www.youtube.com/watch?v=yWXJ-jqg3is")

movieslist =[toy_story,finding_dory,finding_nemo,attack_on_titan]
fresh_tomatoes.open_movies_page(movieslist)
