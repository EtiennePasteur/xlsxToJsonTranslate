# xlsxToJsonTranslate

Simple tool to convert xlsx file to a json object. Built for i18n angular apps

### Usage
```bash
xlsxToJsonTranslate -i <inputfile> -o <outputfile> -l <lang> -k <keycolumn>
```

### Format of xlsx file

| Information | Key | fr | en |
| ----------- | --- | -- | -- |
| Violation - Ajout | rgpd.violation.journey.add.title | Ajout d'une violation de données personnelles | Adding a violation of personal data |
| Violation - Ajout | rgpd.violation.journey.add.step-date.still-alive | La violation est-elle toujours en cours ? | The violation is it ongoing? |
| Violation - Ajout | rgpd.violation.journey.add.step-date.determined-period | La violation s'est étendue sur une période déterminée | The violation was extended over a fixed period |
| Violation - Ajout | rgpd.violation.journey.add.step-date.date-start-violation | Date approximative de la violation | Approximate date of the violation |
| Violation - Ajout | rgpd.violation.journey.add.step-date.date-know-violation | Date et heure de prise de connaissance de la violation | Date and time of becoming aware of the breach |
| Violation - Ajout | rgpd.violation.journey.add.step-date.comments-dates | Commentaires sur les dates | Comments on dates |
| Violation - Ajout | rgpd.violation.journey.add.step-date.discovery-circumstances | Dans quelles circonstances avez-vous découvert la violation ? | Under what circumstances did you discover the violation? |

### Output format

fr.json
```json
{
  "rgpd": {
    "violation": {
      "journey": {
        "add": {
          "title": "Ajout d'une violation de données personnelles",
          "step-date": {
            "still-alive": "La violation est-elle toujours en cours ?",
            "determined-period": "La violation s'est étendue sur une période déterminée",
            "date-start-violation": "Date approximative de la violation",
            "date-know-violation": "Date et heure de prise de connaissance de la violation",
            "comments-dates": "Commentaires sur les dates",
            "discovery-circumstances": "Dans quelles circonstances avez-vous découvert la violation ?"
          }
        }
      }
    }
  }
}
```

en.json
```json
{
  "rgpd": {
    "violation": {
      "journey": {
        "add": {
          "title": "Adding a violation of personal data",
          "step-date": {
            "still-alive": "The violation is it ongoing?",
            "determined-period": "The violation was extended over a fixed period",
            "date-start-violation": "Approximate date of the violation",
            "date-know-violation": "Date and time of becoming aware of the breach",
            "comments-dates": "Comments on dates",
            "discovery-circumstances": "Under what circumstances did you discover the violation?"
          }
        }
      }
    }
  }
}
```
