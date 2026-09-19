{
  IFS= read -r entete
  IFS='|' read -r auteur titre editeur annee isbn presentation
} < data/livres.csv

printf '%s\n' "$auteur"
printf '%s\n' "$titre"
printf '%s\n' "$editeur"
printf '%s\n' "$annee"
printf '%s\n' "$isbn"
printf '%s\n' "$presentation"
