html() {
  printf '%s' "$1" | sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g'
}

pour_sed() {
  sed -e 's/[\\&|]/\\&/g'
}

mkdir -p www/books

num=0

while IFS='|' read -r auteur titre editeur annee isbn presentation
do
  num=$((num + 1))
  titre_sed=$(html "$titre" | pour_sed)
  auteur_sed=$(html "$auteur" | pour_sed)
  editeur_sed=$(html "$editeur" | pour_sed)
  annee_sed=$(html "$annee" | pour_sed)
  isbn_sed=$(html "$isbn" | pour_sed)
  presentation_sed=$(html "$presentation" | pour_sed)
  sed \
    -e "s|%TITRE%|$titre_sed|g" \
    -e "s|%AUTEUR%|$auteur_sed|g" \
    -e "s|%EDITEUR%|$editeur_sed|g" \
    -e "s|%ANNEE%|$annee_sed|g" \
    -e "s|%ISBN%|$isbn_sed|g" \
    -e "s|%PRESENTATION%|$presentation_sed|g" \
    templates/livres.html > "www/books/${num}.html"

done < <(tail -n +2 data/livres.csv)

printf 'Génération finie : %s fiches créées.\n' "$num"
