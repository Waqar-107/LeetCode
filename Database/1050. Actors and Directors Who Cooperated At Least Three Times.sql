SELECT
    ad.actor_id,
    ad.director_id
FROM ActorDirector AS ad
GROUP BY ad.actor_id, ad.director_id
HAVING COUNT(ad.timestamp) >= 3
