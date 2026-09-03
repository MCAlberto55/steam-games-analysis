## Key Questions
**What is the trend for genres and categories in late 2025?**

Both genres and categories have a high number of games labeled as _indie_ and _single-player_, respectively, across all the years the dataset spans. In late 2025, all genres and categories increased while keeping the same proportions as before. Other common genres are _casual_, _adventure_, and _action_. On the other hand, games categorized with Steam features like _Family Sharing_, _Steam Achievements_, and _Steam Cloud_ are also increasing.

        This information lets us conclude that single-player indie games related to adventure and action gameplay are increasing. It is interesting to see that new Steam games are implementing Steam features regardless of genre, even though it is very likely that most of these games are indie.

**Does price truly determine a game's popularity?**

Popularity has limitations when it comes to estimating whether a game is truly successful. Popularity depends on users who decide to leave a recommendation on a game's Steam page. For popular game franchises, this behavior can be explained by the fact that users already know those franchises. However, it is expected that regular users who try a game will simply play it or stop playing it without ever leaving a review on its Steam page. This can be supported by the fact that 56,045 games have 0 recommendations.

        As shown in `Relation between Free/Paid popular games (log1p scale)`, when considering only games with at least 10 recommendations, it appears that a game is more likely to have more recommendations if it is a paid game. Almost all free-to-play games have low popularity.

**What are the primary differences between trends during and after the COVID-19 pandemic?**

Trends in categories, genres, and prices still look the same in the years following the COVID-19 pandemic. The main difference is the number of games released each month and year, which has increased significantly since COVID-19.

        As one would expect, people spent more time on video games and other home activities during COVID-19, which is reflected in the average number of game recommendations during that period. However, even before COVID-19, the trend toward indie, action, and single-player games already existed; it has simply increased in recent years.

**Is it possible to determine whether a game will be successful?**

Unfortunately, more information is needed to determine whether a game is successful. Recommendations only indicate how much people think a game is worth trying, which can serve as an indicator of popularity. Typically, a successful game is defined based on cost and earnings, but we don't have that kind of information or anything else we could use to confidently say "that is a successful game."

## EDA Insights

- On average, 35 games are released every day.
- Within a year, most releases occur during the last trimester (Oct-Dec).
- The COVID-19 pandemic created an opportunity to develop a significant number of games, which led to a notable increase in yearly releases after 2023.
- _Casual_ and _indie_ is one of the most popular genre combinations. _Single-player_ and _Family Sharing_ are the most popular category combinations. However, most games have uncommon combinations, which suggests that these popular genres and categories may simply be the most generic ones, in addition to being the most popular.
- It looks like the trend toward indie games will continue in the coming years. The number of _indie_ games has doubled since 2023, which could possibly be explained by the COVID-19 pandemic.
- Just like _indie_ games, _single-player_ games are a major trend for years to come.
- The median price is around $5, and the most common price is $1.99, which makes sense given the large number of _indie_ games.
- During the COVID-19 pandemic, median prices oscillated between $3 and $5. The median price usually increases at the end of each trimester, when most games are released.
- After the COVID-19 pandemic, the median price in 2025 stayed close to $5 for almost the entire year. This could be caused by the rising costs of hardware required for AI training, which drives prices up.
- Considering all games, the average price increased only slightly during the COVID-19 pandemic.
- Almost 88% of the games in the dataset have 0 recommendations. Most players usually play a game or stop playing it without ever leaving feedback on its Steam page.
- The most recommended games are usually paid games. The most popular free-to-play game is only half as popular as some of the most popular paid games.

## Model training results

- Random Forest was able to learn the split identified by the K-Means and K-Prototypes models.
- Test data was correctly labeled by the resulting models (OHE and weighted), since it follows the same trends.
- Both models perform correctly even on new data, as tested by adding noise to the test data.
- Both models seem to identify 3 types of games, despite the fact that inertia and silhouette scores suggested a different value of k (2):
    - **Prosperous**: Games for which recommendations are the strongest deterministic feature. These are games that are minimally known.
    - **Casual F2P**: An indie, free-to-play, casual, single-player game.
    - **Paid game**: Games similar to _casual F2P_ in terms of genres and categories, but not free-to-play.

However, my goal was to generate clusters that were both distinguishable and easy to interpret. Although OHE is the more technically correct approach, it results in a very simple clustering. On the other hand, weighted genres and categories are a bit harder to interpret for each cluster, but they provide more information about the clustering overall.

## Limitations and subsequent analysis

- The dataset doesn't provide a way to determine whether a game is successful.
- A way to filter out popular franchises would be very useful for identifying anomalous games in terms of success.
- Addressing class imbalance in genres and categories is difficult to carry out because the data is multi-label. Removing a sample doesn't just remove data for one specific genre or category, it also removes information about other genres and categories as collateral damage.
- It would be useful to check whether games are being correctly classified in terms of genres and categories, since some games might have fewer listed characteristics than they actually have. This could be because these values are "popular user-defined" tags, as set on Steam game pages. The most common number of genres per game is 1.
