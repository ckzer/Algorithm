SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE (NAME LIKE '%EL%' or '%eL%' or '%El%' or '%el%') AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC