library(ggplot2)
library(lubridate)

# read ratings, convert time and plot first graph
df <- read.csv(file="dog_ratings.csv",sep="\t",head=T)
df$time <- strptime(as.character(df$time),"%a %b %d %H:%M:%S %z %Y")
ggplot(df,aes(x=df$time,y=as.numeric(as.character(df$rating)))) + geom_point() + theme_minimal() + scale_x_datetime("time") + scale_y_continuous("rating")
ggsave("outlier.png")

# let's remove atticus, cute as he is and convert ratings to numeric
df$rating <- as.numeric(as.character(df$rating))
df$rating
df_no_atticus <- subset(df,df$rating < 1700)

# plot yearwise boxplot
df_no_atticus$year<- year(df_no_atticus$time)
ggplot(df_no_atticus,aes(as.character(year),rating,fill=as.character(year))) + geom_boxplot() + scale_x_discrete("Year") + theme_minimal() + theme(text=element_text(size=15),axis.text=element_text(size=15))+ scale_fill_discrete(guide=FALSE)
ggsave("boxplot_years.png")

# let's do the scatterplot, w/o the outlier
ggplot(df_no_atticus,aes(x=time,y=rating)) + geom_point() + theme_minimal() + scale_x_datetime("time") + scale_y_continuous("rating") + geom_smooth(method="glm")+ theme(text=element_text(size=15),axis.text=element_text(size=15))
ggsave("scatterplot.png")
