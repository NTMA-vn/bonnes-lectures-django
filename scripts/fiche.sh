html() {
  printf '%s' "$1" | sed -e 's/&/\&amp;/g' -e 's/</\&lt;/g' -e 's/>/\&gt;/g'
}

pour_sed() {
  sed -e 's/[\\&|]/\\&/g'
}

titre="La volonté du dragon"
auteur="Lionel Davoust"
editeur="Critic"
annee="2010"
isbn="978-2-9534998-1-0"
presentation="Une reine dont les yeux émeraude lisent l'avenir... Un enfant-roi, passablement fou, gardien d'un savoir oublié... Du déroulement de leur partie d'échecs pourrait bien se décider l'issue de la guerre... Entre les derniers royaumes libres et les forces d'invasion de l'Empire d'Asreth se dresse l'imprenable Qhmarr, petit pays à peine sorti de l'ère médiévale. Gouverné par un roi trop jeune et un conseiller trop confiant, il ne devrait représenter dans le plan de conquête de l'Empire qu'une note de bas de page. Et alors que le généralissime D'eolus Vasteth s'emploie à négocier les modalités d'une reddition diplomatique, déjà, aux portes de la capitale, se presse l'implacable armada... La conclusion du conflit ne fait aucun doute. D'une manière ou d'une autre, Qhmarr passera sous pavillon asrien. Pourtant, malgré la défaite annoncée, Vasteth découvre des dirigeants qhmarri inflexibles, prêts à confier le destin de leur nation à d'absurdes croyances ancestrales. À travers le défi lancé par l'enfant-roi, ce sont toutes les certitudes du généralissime qui vont se voir ébranlées, tandis que, sur la mer, les soldats meurent, simples pions sur un échiquier qui les dépasse... Lionel Davoust est l'auteur d'une dizaine de nouvelles dont « L'île close », lauréate du prix Imaginales 2009, qui a connu une traduction américaine. La Volonté du Dragon développe l'univers d'Évanégyre introduit dans la nouvelle « Bataille pour un Souvenir » (finaliste de la dernière sélection des Utopiales). Avec ce court roman indépendant, il nous plonge dans l'affrontement inégal entre un puissant empire, fort d'avoir dompté une magie par la technologie, et un petit pays au culte passéiste ; l'occasion, pour lui, d'opposer deux façons de penser le monde. Un conflit passionnant où l'on est bien en peine de deviner qui sera mis « échec et mat »."

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
  templates/livres.html > www/books/essai.html

