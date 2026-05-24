import pandas as pd

def calculate_demographic_data(print_data=True):

    # Leer archivo CSV
    df = pd.read_csv('adult.data.csv')

    # ==================================================
    # PREGUNTA 1
    # ¿Cuántas personas hay por raza?
    # ==================================================

    print("\nPREGUNTA 1: Cantidad de personas por raza\n")

    race_count = df['race'].value_counts()

    print(race_count)

    # ==================================================
    # PREGUNTA 2
    # Edad promedio de hombres
    # ==================================================

    print("\nPREGUNTA 2: Edad promedio de hombres\n")

    average_age_men = round(
        df[df['sex'] == 'Male']['age'].mean(),
        1
    )

    print(average_age_men)

    # ==================================================
    # PREGUNTA 3
    # Porcentaje con Bachelor's
    # ==================================================

    print("\nPREGUNTA 3: Porcentaje con Bachelor's\n")

    percentage_bachelors = round(
        df[df['education'] == 'Bachelors'].shape[0]
        / df.shape[0] * 100,
        1
    )

    print(percentage_bachelors)

    # ==================================================
    # PREGUNTA 4
    # Personas con educación avanzada que ganan >50K
    # ==================================================

    print("\nPREGUNTA 4: Educación avanzada con salario >50K\n")

    higher_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    rich = df['salary'] == '>50K'

    higher_education_rich = round(
        (higher_education & rich).sum()
        / higher_education.sum() * 100,
        1
    )

    print(higher_education_rich)

    # ==================================================
    # PREGUNTA 5
    # Personas sin educación avanzada que ganan >50K
    # ==================================================

    print("\nPREGUNTA 5: Sin educación avanzada con salario >50K\n")

    lower_education_rich = round(
        (~higher_education & rich).sum()
        / (~higher_education).sum() * 100,
        1
    )

    print(lower_education_rich)

    # ==================================================
    # PREGUNTA 6
    # Mínimo de horas trabajadas
    # ==================================================

    print("\nPREGUNTA 6: Mínimo de horas trabajadas\n")

    min_work_hours = df['hours-per-week'].min()

    print(min_work_hours)

    # ==================================================
    # PREGUNTA 7
    # Porcentaje de ricos entre quienes trabajan menos horas
    # ==================================================

    print("\nPREGUNTA 7: Porcentaje de ricos entre quienes trabajan menos horas\n")

    min_workers = df['hours-per-week'] == min_work_hours

    rich_percentage = round(
        (min_workers & rich).sum()
        / min_workers.sum() * 100,
        1
    )

    print(rich_percentage)

    # ==================================================
    # PREGUNTA 8
    # País con mayor porcentaje de ricos
    # ==================================================

    print("\nPREGUNTA 8: País con mayor porcentaje de ricos\n")

    country_rich = (
        df[rich]['native-country'].value_counts()
        / df['native-country'].value_counts()
        * 100
    ).sort_values(ascending=False)

    highest_earning_country = country_rich.index[0]

    highest_earning_country_percentage = round(
        country_rich.iloc[0],
        1
    )

    print(highest_earning_country)
    print(highest_earning_country_percentage)

    # ==================================================
    # PREGUNTA 9
    # Ocupación más popular en India (>50K)
    # ==================================================

    print("\nPREGUNTA 9: Ocupación más popular en India (>50K)\n")

    top_IN_occupation = (
        df[
            (df['native-country'] == 'India')
            & rich
        ]['occupation']
        .value_counts()
        .index[0]
    )

    print(top_IN_occupation)

    # ==================================================
    # RETORNO FINAL
    # ==================================================

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
