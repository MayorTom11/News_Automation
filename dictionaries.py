from datetime import date, timedelta

SORT_OPTIONS = {
    "Por Relevancia": "relevancy",
    "Por Fecha": "publishedAt",
    "Por Popularidad": "popularity"
}

DATE_OPTIONS = {
    "Hoy": (date.today(), date.today()),
    "Ayer": (date.today() - timedelta(days=1), date.today() - timedelta(days=1)),
    "Hace 3 días": (date.today() - timedelta(days=3), date.today() - timedelta(days=3)),
    "Hace 5 días": (date.today() - timedelta(days=5), date.today() - timedelta(days=5))
}
