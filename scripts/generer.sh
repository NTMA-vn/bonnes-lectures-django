html() {
  printf '%s' "$1" | sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g'
}

pour_sed() {
  sed -e 's/[\\&|]/\\&/g'
}

mkdir -p www/books

printf '<!doctype html>\n' > www/livres.html
printf '<html lang="fr">\n' >> www/livres.html
printf '<head>\n<meta charset="utf-8">\n<title>Catalogue</title>\n</head>\n' >> www/livres.html
printf '<body>\n' >> www/livres.html
printf '<h1>Catalogue des livres</h1>\n' >> www/livres.html
printf '<p><a href="index.html">Accueil</a></p>\n' >> www/livres.html
printf '<table>\n<tr><th>Auteur</th><th>Titre</th></tr>\n' >> www/livres.html

numero=0

while IFS='|' read -r auteur titre editeur annee isbn presentation
do
  numero=$((numero + 1))

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
    templates/livres.html > "www/books/$numero.html"

  auteur_html=$(html "$auteur")
  titre_html=$(html "$titre")

  printf '<tr><td>%s</td><td><a href="books/%s.html">%s</a></td></tr>\n' "$auteur_html" "$numero" "$titre_html" >> www/livres.html
done < <(tail -n +2 data/livres.csv)

printf '</table>\n' >> www/livres.html
printf '</body>\n' >> www/livres.html
printf '</html>\n' >> www/livres.html
