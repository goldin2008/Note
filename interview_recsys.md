## RecSys powered by LLMs interview prep

### a movie recommender application powered by LLMs
In this chapter, we explored how LLMs could change the way we approach a recommendation system task. We started from the analysis of the current strategies and algorithms for building recommendation applications, differentiating between various scenarios (collaborative filtering, content-based, cold start, etc.) as well as different techniques (KNN, matrix factorization, and NNs).

We then moved to the new, emerging field of research into how to apply the power of LLMs to this field, and explored the various experiments that have been done in recent months.

Leveraging this knowledge, we built a movie recommender application powered by LLMs, using LangChain as the AI orchestrator and Streamlit as the front-end, showing how LLMs can revolutionize this field thanks to their reasoning capabilities as well as their generalization. This was just one example of how LLMs not only can open new frontiers, but can also enhance existing fields of research.

A recommendation system is a computer program that recommends items for users of digital platforms such as e-commerce websites and social networks. It uses large datasets to develop models of users’ likes and interests, and then recommends similar items to individual users.

There are different types of recommendation systems, depending on the methods and data they use. Some of the common types are:
- Collaborative filtering: This type of recommendation system uses the ratings or feedback of other users who have similar preferences to the target user. It assumes that users who liked certain items in the past will like similar items in the future. For example, if user A and user B both liked movies X and Y, then the algorithm may recommend movie Z to user A if user B also liked it.
Collaborative filtering can be further divided into two subtypes: user-based and item-based:
  - User-based collaborative filtering finds similar users to the target user and recommends items that they liked.
  - Item-based collaborative filtering finds similar items to the ones that the target user liked and recommends them.
- Content-based filtering: This type of recommendation system uses the features or attributes of the items themselves to recommend items that are similar to the ones that the target user has liked or interacted with before. It assumes that users who liked certain features of an item will like other items with similar features. The main difference with item-based collaborative filtering is that, while this latter item-based uses patterns of user behavior to make recommendations, content-based filtering uses information about the items themselves. For example, if user A liked movie X, which is a comedy with actor Y, then the algorithm may recommend movie Z, which is also a comedy with actor Y.
- Hybrid filtering: This type of recommendation system combines both collaborative and content-based filtering methods to overcome some of their limitations and provide more accurate and diverse recommendations. For example, YouTube uses hybrid filtering to recommend videos based on both the ratings and views of other users who have watched similar videos, and the features and categories of the videos themselves.
- Knowledge-based filtering: This type of recommendation system uses explicit knowledge or rules about the domain and the user’s needs or preferences to recommend items that satisfy certain criteria or constraints. It does not rely on ratings or feedback from other users, but rather on the user’s input or query. For example, if user A wants to buy a laptop with certain specifications and budget, then the algorithm may recommend a laptop that satisfies those criteria. Knowledge-based recommender systems work well when there is no or little rating history available, or when the items are complex and customizable.

## References

RAG:
>
