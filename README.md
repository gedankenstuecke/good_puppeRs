# good puppeRs
Another nonsensical shower thought I had lately: Have the ratings of [@dog_rates](http://www.twitter.com/dog_rates) increased over time? The account was [started on 2015-11-15](https://twitter.com/dog_rates/status/832088576586297345) and luckily (at least from a scraping point of view) has tweeted only around ~3.5k times. So one can basically scrape all data through the *Twitter* API. Which is what this code does, [read my blogpost with a bit more details](http://ruleofthirds.de/they-are-good-dogs-indeed/) if you want. And, for the fun of it, the citable graphs can be found on *figshare*.

## Usage
- Run `dogrates.py` in order to get all tweets that contain a rated dog.
- Run `plots.R` to get some figures created out of the data.
- Run `pupper_pictures.py` to download the images and bin them according to rating. Bonus: You can use this data right away to re-train *TensorFlow*. :joy:
