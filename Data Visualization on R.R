colnames(Netflix)
view(Netflix)
NetflixMovies <- Netflix[Netflix$Category == "Movie",]
view(NetflixMovies)
NetflixTv <- Netflix[Netflix$Category == "TV Show",]
library(stringr)
NetflixTv
Netflix[c('Minutes','Units')] <- str_split_fixed(Netflix$Duration, ' ', 2)
NetflixMovies[c('Minutes','Units')] <- str_split_fixed(NetflixMovies$Duration, ' ', 2)
ggplot(Netflix, aes(x = Rating, fill = Category, color = Rating)) + geom_bar() + facet_grid(Category~Units)
#Horizontal Barplot
ggplot(Netflix, aes(y = Rating, fill = Category, color = Rating)) + geom_bar()
#Grouped Barplot
ggplot(Netflix, aes(y = Rating), fill = Category, color = Rating) + geom_bar(position = "dodge")
###
ggplot(NetflixTv, aes(x = Rating, y = Minutes, color = Rating)) + geom_boxplot() + labs(y = 'Seasons') + coord_flip()
Netflix[Netflix$Category == "Movie",]
NetflixTv$Release_Date <- dmy(NetflixTv$Release_Date) 
str(Netflix)
Netflix$Release_Date
#LinePlot
ggplot(NetflixTv, aes(x = Release_Date, y = Minutes)) + geom_line()
economics
ggplot(economics, aes(x = date, y = pce)) +geom_line()
#crossTable
library(descr)
ggplot(NetflixTv) + geom_histogram(aes(x = Minutes), stat = "count", binwidth = 0.5)
