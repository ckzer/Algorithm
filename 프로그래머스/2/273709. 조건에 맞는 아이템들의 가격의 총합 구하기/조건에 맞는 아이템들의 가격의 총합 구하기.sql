SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE ITEM_NAME IN (SELECT ITEM_NAME
               FROM ITEM_INFO
               WHERE RARITY='LEGEND')