import csv
import pandas as pd
from datetime import timedelta, date
from django.templatetags.static import static
url = static("data\South_Africa.csv")
vaccines = pd.read_csv(url)

fully_vaccinated_daily=vaccines.people_fully_vaccinated.iloc[-1] - vaccines.people_fully_vaccinated.iloc[-2]

unvaccinated_people = 58560000 - vaccines.people_fully_vaccinated.iloc[-1]

days_unitl_fully_vaccinated = unvaccinated_people/fully_vaccinated_daily

people_need_vacvine_for_herd_immunity = 58560000 * 0.67 - vaccines.people_fully_vaccinated.iloc[-1]

days_until_herd_immunity = people_need_vacvine_for_herd_immunity/fully_vaccinated_daily

EndDate = date.today() + timedelta(days= int(days_until_herd_immunity))
